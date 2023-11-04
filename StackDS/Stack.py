# Queue implementation using Python's deque() class as well as a user defined class for customizability
from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data) -> None:
        self.stack.appendleft(data)  # Appends to the start of deque

    def pop(self):
        return self.stack.popleft()  # Pops the most recent element

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

    def getSize(self) -> int:
        return len(self.stack)

    def top(self):  # Returns the top of the stack. Does not pop!
        return self.stack[0]

    def printStack(self):
        print(self.stack)


# ----- Testing stack functions -----
myStack = Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)

print(myStack.pop())

myStack.printStack()
# ----- Testing stack functions -----




