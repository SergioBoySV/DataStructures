# Queue implementation using Python's deque() class as well as a user defined class for customizability
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data) -> None:
        self.queue.append(data)  # Appends to the end of deque (as a normal list would)

    def dequeue(self):
        return self.queue.popleft()  # Pops from the left (beginning of queue)

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def getSize(self) -> int:
        return len(self.queue)

    def getNext(self) -> int:  # Gets the next in line. Does not pop item.
        return self.queue[0]

    def printQueue(self) -> None:
        print(self.queue)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.printQueue()
print(queue.getNext())

print(queue.dequeue())
queue.printQueue()
print(queue.getNext())

