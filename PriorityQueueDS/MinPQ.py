class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.index = None  # Position in heap array


class PriorityQueue:
    def __init__(self):
        self.size = 0
        self.heap = []  # Array that serves as an implementation for a heap

    def insert(self, node: Node) -> None:
        self.heap.append(node)
        self.buildMinHeap(self.heap)
        self.size += 1

    def remove(self) -> Node:  # AKA extractMax function. Pops and returns the root of the heap. Also reorganizes the heap
        ret = self.heap.pop(0)
        self.buildMinHeap(self.heap)
        self.size -= 1
        return ret

    def getMax(self) -> Node:  # Returns root of the heap. Does not pop!
        return self.heap[0]

    def getSize(self) -> int:
        return self.size

    def minHeapify(self, heap: list, i: int) -> None:  # User should never use this function!
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        smallest = i
        n = len(heap)

        if leftChild < n and heap[leftChild].priority < heap[smallest].priority:
            smallest = leftChild
        if rightChild < n and heap[rightChild].priority < heap[smallest].priority:
            smallest = rightChild
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.minHeapify(heap, smallest)  # Recursive call
        # self.heap[i].index = i  # Works but does not index the middle element (the one we pass in buildMaxHeap)

    def buildMinHeap(self, heap: list) -> None:
        start = len(heap) // 2 - 1
        for i in range(start, -1, -1):
            self.minHeapify(heap, i)

    def printPQRec(self, root) -> None:
        leftChild = 2 * root.index + 1
        rightChild = 2 * root.index + 2

        print(f'{root.data} ', end='')
        # The following if statements help to determine if we're at a leaf node, if we are, break out
        # This traversal may not be right, get it checked!!!!!
        if leftChild >= self.size:
            return
        else:
            self.printPQRec(self.heap[leftChild])
        if rightChild >= self.size:
            return
        else:
            self.printPQRec(self.heap[rightChild])

    def printPQ(self) -> None:
        # self.printPQRec(self.heap[0])
        # print('')
        for i in range(len(self.heap)):  # Iterative approach
            print(self.heap[i].data, end=' ')
        print('')

    def printPQAsTree(self) -> None:
        # for i in range(self.size):
        #     print('\t', end='')
        # print('\t\t\t\tRoot\n\t\t\t\t/\\\n\t\t\t\tC1\tC2')  # Something like this
        pass


# Testing PQ functions
myPQ = PriorityQueue()

myPQ.insert(Node('Sergio', 20))  # 3
myPQ.insert(Node('Rafael', 45))  # 1
myPQ.insert(Node('Javier', 13))  # 5
myPQ.insert(Node('Sofia', 6))  # 6
myPQ.insert(Node('Betty', 44))  # 2
myPQ.insert(Node('Josue', 18))  # 4

myPQ.printPQ()
print(f'PQs Size = {myPQ.getSize()}')

print(f'PQs Min = {myPQ.remove().priority}')
myPQ.printPQ()
print(f'PQs Size = {myPQ.getSize()}')

myPQ.insert(Node('Rando', 0))
myPQ.printPQ()


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
