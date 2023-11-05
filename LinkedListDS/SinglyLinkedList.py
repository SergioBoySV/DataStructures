class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode(data):
    createdNode = Node(data)
    createdNode.next = None
    createdNode.index = None
    return createdNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):  # Allows for iteration through the linked list
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insertAtBeginning(self, newNode):
        if not isinstance(newNode, Node):
            newNode = createNode(newNode)

        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return

    def insertAtEnd(self, newNode, tailNode=None):
        if tailNode is not None:
            tailNode.next = newNode
            # self.tail = newNode
            return

        if not isinstance(newNode, Node):
            newNode = createNode(newNode)
        if self.isEmpty():
            self.head = newNode
            self.size += 1
            return
        for node in self:  # iterate until we get to the last element
            pass
        node.next = newNode
        self.size += 1
        # tmpHead = self.head
        # while tmpHead.next is not None:  # Another method using a while loop
        #     tmpHead = tmpHead.next
        # tmpHead.next = node

    def insertAfter(self, targetNode, newNode):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        if not isinstance(newNode, Node):
            newNode = createNode(newNode)

        if isinstance(targetNode, Node):
            # if self.tail.data == targetNode.data:
            #     self.insertAtEnd(newNode, tailNode=self.tail)
            #     return
            newNode.next = targetNode.next
            targetNode.next = newNode
            return

        if not isinstance(targetNode, Node):
            # if self.tail.data == targetNode:  # If trying to insert after tail, call insertAtEnd
            #     return self.insertAtEnd(newNode)
            for node in self:
                if node.data == targetNode:
                    newNode.next = node.next
                    node.next = newNode
                    self.size += 1
                    return

        raise Exception(f'Node with data: {targetNode} does not exist!')

    def insertBefore(self, targetNode, newNode):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        if not isinstance(newNode, Node):
            newNode = createNode(newNode)
        if not isinstance(targetNode, Node):
            targetNode = createNode(targetNode)

        if self.head.data == targetNode.data:
            return self.insertAtBeginning(newNode)

        previousNode = self.head
        for node in self:
            if node.data == targetNode.data:
                previousNode.next = newNode
                newNode.next = node
                self.size += 1
                return
            previousNode = node

        raise Exception(f'Node with data: {targetNode} does not exist!')

    def removeNode(self, targetNode):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        if not isinstance(targetNode, Node):
            targetNode = createNode(targetNode)

        if self.head.data == targetNode.data:
            return self.removeHead()
        # if self.tail.data == targetNode.data:
        #     return self.removeTail()
        previousNode = self.head
        for node in self:
            if node.data == targetNode.data:
                previousNode.next = node.next
                self.size -= 1
                return
            previousNode = node

        raise Exception(f'Node with data: {targetNode.data} does not exist!')

    def removeHead(self):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        self.head = self.head.next
        self.size -= 1

    def removeTail(self):  # Needs work
        if self.isEmpty():
            raise Exception('Linked List is empty')
        del self.tail
        for node in self:  # iterate until we get to the last element
            pass
        self.tail = node
        self.size -= 1

    def getSize(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.head is None

    def insertAtIndex(self, node: Node, i: int):  # Inserts after the index
        pass

    def removeAtIndex(self, index: int):
        pass

    def search(self, searchValue) -> Node:
        if self.isEmpty():
            raise Exception('Linked List is empty')
        if not isinstance(searchValue, Node):
            searchValue = createNode(searchValue)
        for node in self:
            if node.data == searchValue.data:
                return node
        raise Exception(f'Element {searchValue.data} does not exist in Linked List!')

    def printLinkedList(self) -> None:
        for node in self:
            print(f'{node.data} --> ', end='')
        print('None')


# ----- Testing Linked List -----
myLL = LinkedList()
# array = [1, 10, 2, 20, 3, 30, 50]
#
# for i in array:
#     myLL.insertAtEnd(i)
#
# myLL.printLinkedList()

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)
Node5 = Node(100)
Node6 = Node(110)
Node7 = Node(-1)

myLL.insertAtBeginning(Node1)
myLL.insertAtEnd(Node2)
myLL.insertAtEnd(Node3)
myLL.insertAfter(Node2, Node7)
myLL.insertBefore(Node3, Node6)
myLL.removeNode(Node7)
myLL.insertBefore(Node1, Node7)
myLL.insertAfter(Node3, Node5)
myLL.printLinkedList()

# myLL.insertAtBeginning(1)
# myLL.insertAtEnd(2)
# myLL.insertAtEnd(3)
# myLL.insertAfter(2, 2.5)
# myLL.insertBefore(2, 1.5)
# myLL.removeNode(2)
# myLL.printLinkedList()


'''
Sources:
https://realpython.com/linked-lists-python/  GREAT SOURCE!
https://www.geeksforgeeks.org/insert-node-at-the-end-of-a-linked-list/
'''
