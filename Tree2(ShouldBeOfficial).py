class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.height = None


def getSubTreeHeight(root: Node) -> int:
    if root is None:
        return 0
    return root.height


def updateHeights(root: Node):
    if root is not None:
        root.height = getSubTreeHeight(root.left) if getSubTreeHeight(root.left) > getSubTreeHeight(root.right) else getSubTreeHeight(root.right)
        root.height = root.height + 1
        updateHeights(root.parent)


def attachChildNodes(root: Node, left: Node | None, right: Node | None) -> None:
    root.left = left
    root.right = right

    if left is not None:
        root.left.parent = root
    if right is not None:
        root.right.parent = root
    updateHeights(root)


def createNode(data) -> Node:
    newNode = Node(data)
    newNode.height = 1
    newNode.parent = None
    attachChildNodes(newNode, None, None)

    return newNode


class Tree:
    def insert(self, node: Node, insertValue) -> Node:
        if node is None:
            return createNode(insertValue)

        if insertValue < node.data:
            node.left = self.insert(node.left, insertValue)
        elif insertValue > node.data:
            node.right = self.insert(node.right, insertValue)

        updateHeights(node)
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

tree = Tree()
root = createNode(30)
tree.insert(root, root.data)

tree.insert(root, 20)
tree.insert(root, 40)
tree.insert(root, 70)
tree.insert(root, 60)
tree.insert(root, 80)
print(f'height: {root.height}')
tree.printTree(root)




# testNode = tree.createNode(20)
# print(f"data: {testNode.data}")
# print(f"left child: {testNode.left}")
# print(f"right child: {testNode.right}")
# print(f"height: {testNode.height}")
