# Queue implementation using Python's deque() class as well as a user defined class for customizability
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data) -> None:
        self.buffer.appendleft(data)

    def dequeue(self):  # Returns any
        return self.buffer.pop()

    def isEmpty(self) -> bool:
        return len(self.buffer) == 0  # returns True or False

    def getSize(self) -> int:
        return len(self.buffer)

    def getNext(self) -> int:  # Gets the next in line. Does not pop item.
        return self.buffer[-1]

    def printQueue(self) -> None:
        print(self.buffer)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.printQueue()
print(queue.getNext())

print(queue.dequeue())
queue.printQueue()

