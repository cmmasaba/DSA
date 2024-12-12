'''
Implementation of a heap data structure
'''

class Heap:

    def __init__(self, array: list):
        self.heap: list = array
        self.heap_size: int = len(self.heap)
        self.build_max_heap()
    
    def parent(self, index):
        return index // 2
    
    def left(self, index):
        return 2 * index
    
    def right(self, index):
        return (2 * index) + 1
    
    def max_heapify(self, index = 0):
        '''
        Maintain the max-heap property

        Args:
        :param index: the index of the subtree to maintain max-heap property from.
        '''
        left = self.left(index)
        right = self.right(index)

        if left <= self.heap_size and self.heap[left] > self.heap[index]:
            largest = left
        else:
            largest = index
        
        if right <= self.heap_size and self.heap[right] > self.heap[index]:
            largest = right
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)

    def min_heapify(self, index = 0):
        '''
        Maintain the min-heap property

        Args:
        :param index: the index of the subtree to maintain min-heap property from.
        '''
        left = self.left(index)
        right = self.right(index)

        if left <= self.heap_size and self.heap[left] < self.heap[index]:
            smallest = left
        else:
            smallest = index
        
        if right <= self.heap_size and self.heap[right] < self.heap[index]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.min_heapify(smallest)
    
    def build_max_heap(self):
        '''
        Build a max heap from a list of elements.
        '''
        for index in range(len(self.heap) // 2, 1, -1):
            self.max_heapify(index)
    
    def build_min_heap(self):
        '''
        Build a min heap from a list of elements.
        '''
        for index in range(len(self.heap) // 2, 1, -1):
            self.min_heapify(index)