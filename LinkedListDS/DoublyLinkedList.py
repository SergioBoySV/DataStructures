class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.index = None  # Tracks the index of the node. May make insertAtIndex possible, but maybe not


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
        self.head.prev = newNode
        self.head = newNode
        self.size += 1

    def insertAtEnd(self, newNode: Node):
        if self.isEmpty():
            return self.insertAtBeginning(newNode)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def insertAfter(self, targetNodeData, newNode: Node):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        for node in self:
            if node.data == targetNodeData:
                node.next = newNode
                newNode.next = node.next
                newNode.prev = node
                self.size += 1
                return
        raise Exception(f'Node with data: {targetNodeData} does not exist!')

    def insertBefore(self, targetNodeData, newNode: Node):
        if self.isEmpty():
            raise Exception('Linked List is empty')
        if self.head.data == targetNodeData:  # If trying to insert before head, call insertAtBeginning
            return self.insertAtBeginning(newNode)
        for node in self:
            if node.data == targetNodeData:
                newNode.next = node
                newNode.prev = node.prev

    def isEmpty(self) -> bool:
        return self.head is None

    def getSize(self) -> int:
        return self.size






