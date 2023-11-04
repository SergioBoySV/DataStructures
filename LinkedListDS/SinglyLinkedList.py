class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.index = None  # Tracks index of the node. May make insertAtIndex possible, but maybe not


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

    def insertAtBeginning(self, newNode: Node):
        newNode.next = self.head
        self.head = newNode  # New head is newNode
        self.size += 1

    def insertAtEnd(self, newNode: Node):
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

    def insertAfter(self, targetNodeData, newNode: Node):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        # if self.tail.data == targetNodeData:  # If trying to after before tail, call insertAtEnd
        #     return self.insertAtEnd(newNode)
        for node in self:
            if node.data == targetNodeData:
                newNode.next = node.next
                node.next = newNode
                self.size += 1
                return
        raise Exception(f'Node with data: {targetNodeData} does not exist!')

    def insertBefore(self, targetNodeData, newNode: Node):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        if self.head.data == targetNodeData:  # If trying to insert before head, call insertAtBeginning
            return self.insertAtBeginning(newNode)
        previousNode = self.head
        for node in self:
            if node.data == targetNodeData:
                previousNode.next = newNode
                newNode.next = node
                self.size += 1
                return
            previousNode = node
        raise Exception(f'Node with data: {targetNodeData} does not exist!')

    def removeNode(self, targetNodeData):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        if self.head.data == targetNodeData:
            self.head = self.head.next
            self.size -= 1
            return
        previousNode = self.head
        for node in self:
            if node.data == targetNodeData:
                previousNode.next = node.next
                self.size -= 1
                return
            previousNode = node
        raise Exception(f'Node with data: {targetNodeData} does not exist!')

    def removeHead(self):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        self.head = self.head.next
        self.size -= 1

    def removeTail(self):
        self.size -= 1
        pass

    def getSize(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.head is None

    def insertAtIndex(self, node: Node, i: int):  # Inserts after the index
        pass

    def removeAtIndex(self, index: int):
        pass

    def printLinkedList(self) -> None:
        for node in self:
            print(f'{node.data} --> ', end='')
        print('None')


# ----- Testing Linked List -----
myLL = LinkedList()
print(myLL.getSize())
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)
Node5 = Node(100)
Node6 = Node(110)
Node7 = Node(-1)

myLL.insertAtBeginning(Node1)
myLL.insertAtBeginning(Node2)
myLL.insertAtBeginning(Node3)
myLL.insertAtBeginning(Node4)

myLL.insertAtEnd(Node5)
myLL.insertAfter(10, Node6)
myLL.insertBefore(20, Node7)

myLL.removeNode(-1)
myLL.removeHead()

myLL.printLinkedList()
print(myLL.getSize())


'''
Sources:
https://realpython.com/linked-lists-python/  GREAT SOURCE!
https://www.geeksforgeeks.org/insert-node-at-the-end-of-a-linked-list/
'''
