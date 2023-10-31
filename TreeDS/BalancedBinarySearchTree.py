# This is a Tree with balancing capabilities (BBST)

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.height = None


class Tree:
    # def __init__(self, root):
    #     self.root = self.createNode(root)

    # def __init__(self):
    #     self.root = None

    def createNode(self, data) -> Node:
        newNode = Node(data)
        newNode.height = 1
        newNode.parent = None
        self.attachChildNodes(newNode, None, None)

        return newNode

    def attachChildNodes(self, root: Node, left: Node | None, right: Node | None) -> None:
        root.left = left
        root.right = right

        if left is not None:
            root.left.parent = root
        if right is not None:
            root.right.parent = root
        self.updateHeights(root)

    def updateHeights(self, root: Node):
        if root is not None:
            root.height = self.getHeight(root.left) if self.getHeight(root.left) > self.getHeight(
                root.right) else self.getHeight(root.right)
            root.height = root.height + 1
            self.updateHeights(root.parent)

    def getHeight(self, root: Node) -> int:
        if root is None:
            return 0
        return root.height

    def insert(self, node: Node, insertValue) -> Node:
        if node is None:
            return self.createNode(insertValue)

        if insertValue < node.data:
            node.left = self.insert(node.left, insertValue)
        elif insertValue > node.data:
            node.right = self.insert(node.right, insertValue)

        self.updateHeights(node)
        # self.rebalanceTree(node)
        return node

    def search(self, node: Node, query) -> Node:
        if node is None or node.data == query:
            return node

        if query < node.data:
            return self.search(node.left, query)
        elif query > node.data:
            return self.search(node.right, query)

    def deleteNode(self, node: Node, deleteValue) -> Node | None:  # double check what this one is doing
        if node is None:
            return None

        if deleteValue < node.data:
            node.left = self.deleteNode(node.left, deleteValue)
        elif deleteValue > node.data:
            node.right = self.deleteNode(node.right, deleteValue)
        else:  # Reach the node to be deleted
            if node.left is None and node.right is None:
                del node

            elif node.left is None:
                temp = node.right
                del node
                return temp

            elif node.right is None:
                temp = node.left
                del node
                return temp

        return node

    def getBalance(self, root: Node):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, oldRoot: Node):

        if oldRoot is None:
            print("ERROR - Attempting a leftRotate on a NULL Root.")
            return

        newRoot = oldRoot.right

        if newRoot is None:
            print("ERROR - Attempting a leftRotate on a node with no right child (i.e. right child is NULL).")
            return

        if oldRoot.parent is not None:
            if oldRoot.parent.right == oldRoot:
                oldRoot.parent.right = oldRoot.right
            else:
                oldRoot.parent.left = oldRoot.right
        else:
            # treeRoot = newRoot
            self.root = newRoot

        newRoot.parent = oldRoot.parent
        oldRoot.right = newRoot.left

        if newRoot.left is not None:
            newRoot.left.parent = oldRoot

        oldRoot.parent = newRoot
        newRoot.left = oldRoot

        self.updateHeights(oldRoot)

    def rightRotate(self, oldRoot: Node):
        if oldRoot is None:
            print("ERROR - Attempting a rightRotate on a NULL Root.")
            return

        newRoot = oldRoot.left

        if newRoot is None:
            print("ERROR - Attempting a rightRotate on a node with no left child (i.e. left child is NULL).")
            return

        if oldRoot.parent is not None:
            if oldRoot.parent.left == oldRoot:
                oldRoot.parent.left = oldRoot.left
            else:
                oldRoot.parent.right = oldRoot.left
        else:
            # treeRoot = newRoot
            self.root = newRoot

        newRoot.parent = oldRoot.parent
        oldRoot.left = newRoot.right

        if newRoot.right is not None:
            newRoot.right.parent = oldRoot

        oldRoot.parent = newRoot
        newRoot.right = oldRoot

        self.updateHeights(oldRoot)

    def rebalanceTree(self, x: Node):
        while x is not None:
            balanceX = self.getBalance(x)

            if balanceX >= 2 or balanceX <= -2:
                if self.getHeight(x.left) > self.getHeight(x.right):
                    z = x.left
                else:
                    z = x.right

                balanceZ = self.getBalance(z)

                if (balanceX < 0 < balanceZ) or (balanceX > 0 > balanceZ):
                    if balanceZ > 0:
                        self.rightRotate(z)
                    else:  # balanceZ < 0
                        self.leftRotate(z)

                if balanceX >= 2:
                    self.rightRotate(x)
                else:  # balanceX <= -2
                    self.leftRotate(x)
            x = x.parent

    def sortedArrayToBST(self, array, start, end):
        if start > end:
            return

        mid = (start + end) // 2
        root = self.createNode(array[mid])

        root.left = self.sortedArrayToBST(array, start, mid - 1)
        root.right = self.sortedArrayToBST(array, mid + 1, end)
        self.updateHeights(root)

        return root

    def inOrderTraversal(self, root: Node) -> None:
        if root is not None:
            self.inOrderTraversal(root.left)
            print(root.data)
            self.inOrderTraversal(root.right)

    def preOrderTraversal(self, root: Node) -> None:
        if root is not None:
            print(root.data)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    def postOrderTraversal(self, root: Node) -> None:
        if root is not None:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.data)

    def printTree(self, root: Node) -> None:
        i = 1
        if root is not None:
            self.printTree(root.left)

            while i < root.height:
                print('\t', end='')
                i += 1
            print(f'{root.data}')
            self.printTree(root.right)


# Testing tree insertion
tree = Tree()
root = tree.createNode(30)
tree.insert(root, root.data)

print('-'*30)
print(f'Tree before inserting (just the root):')
tree.printTree(root)
print(f'\nTree height before inserting: {root.height}')
print('-'*30)

print('')
print('-'*30)

tree.insert(root, 20)
tree.insert(root, 40)
tree.insert(root, 70)
tree.insert(root, 60)
tree.insert(root, 80)

print(f'Tree after inserting (unbalanced for now :( ):\n')
tree.printTree(root)
print(f'\nTree height after inserting: {root.height}')
print('-'*30)

print('In order traversal of tree:')
tree.inOrderTraversal(root)


# Testing node creation
# testNode = tree.createNode(20)
# print(f"data: {testNode.data}")
# print(f"left child: {testNode.left}")
# print(f"right child: {testNode.right}")
# print(f"height: {testNode.height}")


# Testing sortedArrayToBST
# sortedArray = [9, 10, 15, 30, 35, 42, 46, 50, 57, 61, 67, 72, 78, 80, 89]
# tree = Tree()
# root = tree.sortedArrayToBST(sortedArray, 0, len(sortedArray) - 1)
# tree.printTree(root)
# print(root.height)
