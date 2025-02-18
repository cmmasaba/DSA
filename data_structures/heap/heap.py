'''
Implementation of a heap data structure
'''
from typing import List

class Heap:

    def __init__(self, array: List[int], max=True):
        self.heap: list = array
        self.heap_size: int = len(self.heap)
        self.max_heap = max
        if not self.max_heap:
            self.build_min_heap()
        else:
            self.build_max_heap()
    
    def parent(self, index):
        return index // 2
    
    def left(self, index):
        return 2 * index
    
    def right(self, index):
        return (2 * index) + 1
    
    def max_heapify(self, index = 1):
        '''
        Maintain the max-heap property

        Args:
        :param index: the index of the subtree to maintain max-heap property from.
        '''
        left = self.left(index)
        right = self.right(index)

        if left <= self.heap_size and self.heap[left - 1] > self.heap[index - 1]:
            largest = left
        else:
            largest = index
        
        if right <= self.heap_size and self.heap[right - 1] > self.heap[largest - 1]:
            largest = right
        
        if largest != index:
            self.heap[index - 1], self.heap[largest - 1] = self.heap[largest - 1], self.heap[index - 1]
            self.max_heapify(largest)

    def min_heapify(self, index = 1):
        '''
        Maintain the min-heap property

        Args:
        :param index: the index of the subtree to maintain min-heap property from.
        '''
        left = self.left(index)
        right = self.right(index)

        if left <= self.heap_size and self.heap[left - 1] < self.heap[index - 1]:
            smallest = left
        else:
            smallest = index
        
        if right <= self.heap_size and self.heap[right - 1] < self.heap[smallest - 1]:
            smallest = right
        
        if smallest != index:
            self.heap[index - 1], self.heap[smallest - 1] = self.heap[smallest - 1], self.heap[index - 1]
            self.min_heapify(smallest)
    
    def build_max_heap(self):
        '''
        Build a max heap from a list of elements.
        '''
        n = len(self.heap)
        for index in range((n // 2), 0, -1):
            self.max_heapify(index)
    
    def build_min_heap(self):
        '''
        Build a min heap from a list of elements.
        '''
        n = len(self.heap)
        for index in range((n // 2), 0, -1):
            self.min_heapify(index)


    def heapsort(self):
        if self.max_heap:
            self.max_heap_sort()
        else:
            self.min_heap_sort()

    def max_heap_sort(self):
        self.build_max_heap()
        n = self.heap_size
        for index in range(n, 1, -1):
            self.heap[0], self.heap[index - 1] = self.heap[index - 1], self.heap[0]
            self.heap_size = self.heap_size - 1
            self.max_heapify(1)

    def min_heap_sort(self):
        self.build_min_heap()
        n = self.heap_size
        for index in range(n, 1, -1):
            self.heap[0], self.heap[index - 1] = self.heap[index - 1], self.heap[0]
            self.heap_size = self.heap_size - 1
            self.min_heapify(1)

    def print_heap(self):
        n = len(self.heap)
        for index in range(len(self.heap)):
            print(self.heap[index], end=', ' if index != n-1 else '\n')
        print()


def main():
    array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = Heap(array, max=False)
    heap.print_heap()
    heap.heapsort()
    heap.print_heap()


if __name__ == "__main__":
    main()