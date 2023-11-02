# This is essentially an implementation of a PQ where instead of inserting, you make a heap out of an existing array
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.index = None  # Position in heap array


class PriorityQueue:
    def __init__(self):
        self.size = 0
        self.heap = []  # Array that serves as an implementation for a heap

    def insert(self, node: Node):
        pass

    def remove(self):  # Pops and returns the root of the heap. Also reorganizes the heap (extractMax)
        pass

    def maxHeapify(self, arr: list, i: int) -> None:
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        largest = i
        n = len(arr)

        if leftChild < n and arr[leftChild] > arr[largest]:
            largest = leftChild
        if rightChild < n and arr[rightChild] > arr[largest]:
            largest = rightChild
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.maxHeapify(arr, largest)  # Recursive call

    def minHeapify(self, arr: list, i: int) -> None:
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        smallest = i
        n = len(arr)

        if leftChild < n and arr[leftChild] < arr[smallest]:
            smallest = leftChild
        if rightChild < n and arr[rightChild] < arr[smallest]:
            smallest = rightChild
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.minHeapify(arr, smallest)

    def buildMaxHeap(self, arr: list):
        start = len(arr) // 2 - 1
        for i in range(start, -1, -1):
            self.maxHeapify(arr, i)

    def buildMinHeap(self, arr: list):
        start = len(arr) // 2 - 1
        for i in range(start, -1, -1):
            self.minHeapify(arr, i)

    def getSize(self):
        return self.size

    def printPQ(self, heap: list) -> None:
        for i in range(len(heap)):
            print(heap[i], end=' ')
        print()
        # Instead of iterating through the whole array, perhaps try printing root, then children via the equation above??
        # And if a leaf node, then don't print anything!

# array = [1, 4, 3, 8, 7, 9, 10]
array1 = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
array2 = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
maxPQ = PriorityQueue()
minPQ = PriorityQueue()

maxPQ.buildMaxHeap(array1)
minPQ.buildMinHeap(array2)

maxPQ.printPQ(array1)
print('')
minPQ.printPQ(array2)

'''
Sources:
Heapify Functions - 
https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/#:~:text=Based%20on%20heap%20structure%2C%20priority,maximum%20element%20from%20the%20Arr.
https://www.geeksforgeeks.org/building-heap-from-array/


'''
