from typing import Generic, List, TypeVar

T = TypeVar('T')

class MaxHeap(Generic[T]):

    def __init__(self, arr: List[T] = [], capacity = 10):
        
        self.heap: List[T] = [i for i in arr]
        self.size: int = len(self.heap)
        self.capacity: int = capacity

        if self.size > self.capacity:
            raise Exception('Size greater than capacity')

        if self.size > 0:
            self.heapify()

    def swap(self, i, j):
        
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp
    
    def parent_index(self, i):
        
        if i < self.size:
            return (i - 1)//2
        
        raise Exception('Heap out of bound')
    
    def left_child_index(self, i):
        return 2*i + 1
    
    def right_child_index(self, i):
        return 2*i + 2
    
    def sift_up(self, i):

        while i > 0 and self.heap[i] > self.heap[self.parent_index(i)]:
            
            # Swap
            p_idx = self.parent_index(i)
            self.swap(i, p_idx)

            i = p_idx
    
    def sift_down(self, i):

        max_idx = i

        l_idx = self.left_child_index(i)

        if l_idx < self.size and self.heap[l_idx] > self.heap[i]:
            max_idx = l_idx
        

        r_idx = self.right_child_index(i)

        if r_idx < self.size and self.heap[r_idx] > self.heap[max_idx]:
            max_idx = r_idx
        
        if not i == max_idx:
            self.swap(i, max_idx)
            self.sift_down(max_idx)
    
    def insert(self, element: T):
        self.size += 1
        self.heap.append(element)
        self.sift_up(self.size - 1)
    
    def extract_max(self):
        
        tmp = self.heap[0]
        self.size -= 1
        last_val = self.heap.pop()
        
        if self.size > 0:
            self.heap[0] = last_val
            self.sift_down(0)

        return tmp
    
    def heapify(self):

        p_idx = self.parent_index(self.size - 1)

        for i in range(p_idx, -1, -1):
            self.sift_down(i)
    
    def heap_sort(self):

        n = self.size
        arr = [0] * n

        for i in range(n - 1, -1, -1):
            val = self.extract_max()
            arr[i] = val
        
        return arr
