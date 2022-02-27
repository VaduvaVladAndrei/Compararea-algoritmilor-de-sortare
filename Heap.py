class Heap:
    def __init__(self, heap):
        self.heap = heap
        self.heap_size = len(self.heap)

        self.buildHeap()

    @staticmethod
    def parent(index):
        if index != 0:
            return (index - 1) // 2
        else:
            return -1

    @staticmethod
    def left(index):
        return (2 * index) + 1

    @staticmethod
    def right(index):
        return (2 * index) + 2

    def heapify(self, index):
        left = self.left(index)
        right = self.right(index)

        if left < self.heap_size and self.heap[left] > self.heap[index]:
            largest = left
        else:
            largest = index
        if right < self.heap_size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)

    def buildHeap(self):
        for i in range((self.heap_size - 1) // 2, -1, -1):
            self.heapify(i)

    def insert(self, key):
        self.heap_size += 1
        self.heap.append(key)
        i = self.heap_size - 1
        while i > 0 and self.heap[self.parent(i)] < key:
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)
        self.heap[i] = key


def heapSort(array):
    h = Heap(array.copy())
    for i in range(h.heap_size - 1, -1, -1):
        h.heap[0], h.heap[i] = h.heap[i], h.heap[0]
        array[i] = h.heap.pop()
        h.heap_size -= 1
        h.heapify(0)
