class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head



    def insertAtEnd(self, data):
        pass

    def insertAtIndex(self, data):
        pass

    def removeAtIndex(self, index: int):
        pass

    def removeHead(self):
        pass

    def removeTail(self):
        pass

    def getSize(self) -> int:
        pass

    def printLinkedList(self):


