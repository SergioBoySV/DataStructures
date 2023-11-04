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

    def __iter__(self):  # Allows for iteration through the linked list
        node = self.head
        while node is not None:
            yield node
            node = node.next





