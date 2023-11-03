# Implementations
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.index = None  # Position in heap array


class PriorityQueue:
    def __init__(self):
        self.heap = []  # Array that serves as an implementation for a heap

    def insert(self, node: Node) -> None:
        self.heap.append(node)
        self.buildMaxHeap(self.heap)

    def remove(self) -> Node:  # AKA extractMax function. Pops and returns the root of the heap. Also reorganizes the heap
        ret = self.heap.pop(0)
        self.buildMaxHeap(self.heap)
        return ret

    def getMax(self) -> Node:  # Returns root of the heap. Does not pop!
        return self.heap[0]

    def getSize(self) -> int:
        return len(self.heap)

    def maxHeapify(self, heap: list, i: int) -> None:  # User should never use this function!
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        largest = i
        n = self.getSize()

        if leftChild < n and heap[leftChild].priority > heap[largest].priority:
            largest = leftChild
        if rightChild < n and heap[rightChild].priority > heap[largest].priority:
            largest = rightChild
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            self.maxHeapify(heap, largest)  # Recursive call
        # self.heap[i].index = i  # Works but does not index the middle element (the one we pass in buildMaxHeap)

    def buildMaxHeap(self, heap: list) -> None:
        start = self.getSize() // 2 - 1
        for i in range(start, -1, -1):
            self.maxHeapify(heap, i)

    def printPQRec(self, root) -> None:
        leftChild = 2 * root.index + 1
        rightChild = 2 * root.index + 2

        print(f'{root.data} ', end='')
        # The following if statements help to determine if we're at a leaf node, if we are, break out
        # This traversal may not be right, get it checked!!!!!
        if leftChild >= self.getSize():
            return
        else:
            self.printPQRec(self.heap[leftChild])
        if rightChild >= self.getSize():
            return
        else:
            self.printPQRec(self.heap[rightChild])

    def printPQ(self) -> None:
        # self.printPQRec(self.heap[0])
        # print('')
        for i in range(self.getSize()):  # Iterative approach
            print(self.heap[i].priority, end=' ')
        print('')

    def printPQAsTree(self) -> None:
        # for i in range(self.size):
        #     print('\t', end='')
        # print('\t\t\t\tRoot\n\t\t\t\t/\\\n\t\t\t\tC1\tC2')  # Something like this
        pass


# ----- Testing PQ functions via insertion -----
myPQ = PriorityQueue()

Sergio = Node('Sergio', 20)
Rafael = Node('Rafael', 45)
Javier = Node('Javier', 13)
Sofia = Node('Sofia', 6)
Betty = Node('Betty', 44)
Josue = Node('Josue', 18)

Sergio.index = 4
Rafael.index = 0
Javier.index = 5
Sofia.index = 3
Betty.index = 1
Josue.index = 2

myPQ.insert(Sergio)
myPQ.insert(Rafael)
myPQ.insert(Javier)
myPQ.insert(Sofia)
myPQ.insert(Betty)
myPQ.insert(Josue)

# myPQ.insert(Node('Sergio', 20))  # 3
# myPQ.insert(Node('Rafael', 45))  # 1
# myPQ.insert(Node('Javier', 13))  # 5
# myPQ.insert(Node('Sofia', 6))  # 6
# myPQ.insert(Node('Betty', 44))  # 2
# myPQ.insert(Node('Josue', 18))  # 4

myPQ.printPQ()
print(f'PQs Size = {myPQ.getSize()}')

print(f'PQs Max = {myPQ.remove().priority}')
myPQ.printPQ()
print(f'PQs Size = {myPQ.getSize()}')
# ----- Testing PQ functions via insertion -----


'''
Sources:
Heapify Functions - 
https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/#:~:text=Based%20on%20heap%20structure%2C%20priority,maximum%20element%20from%20the%20Arr.
https://www.geeksforgeeks.org/building-heap-from-array/
https://www.geeksforgeeks.org/binary-heap/

PQ General Info - 
https://www.geeksforgeeks.org/priority-queue-set-1-introduction/
https://stackoverflow.com/questions/18993269/difference-between-priority-queue-and-a-heap
https://stackoverflow.com/questions/65882138/implementing-priority-queue-using-max-heap-vs-balanced-bst
'''
