from heapq import heapify, heappop, heappush, heappushpop

class PriorityQueue:
    # heap: list
    def __init__(self, heap = []):
        self.heap = heap
        heapify(self.heap)
    
    def push(self, item):
        heappush(self.heap, item)
    
    def pop(self):
        return heappop(self.heap)
    
    def pushpop(self, item):
        return heappop(self.heap, item)
    
    def __call__(self):
        return self.heap
    
    def __len__(self):
        return len(self.heap)
    
    def size(self):
        return len(self.heap)
    
    def empty(self):
        return len(self.heap) == 0
    
    def front(self):
        return self.heap[0]
