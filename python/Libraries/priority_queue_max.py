import heapq

class PriorityQueue_max:
    # heap: list
    def __init__(self, heap):
        self.heap = heap
        heapq.heapify(self.heap)
    
    def push(self, item):
        heapq.heappush(self.heap, (-1) * item)
    
    def pop(self):
        return (-1) * heapq.heappop(self.heap)
    
    def pushpop(self, item):
        return (-1) * heapq.heappop(self.heap, (-1) * item)
    
    def __call__(self):
        return [-i for i in self.heap]
    
    def __len__(self):
        return len(self.heap)
    
    def empty(self):
        return len(self.heap) == 0
    
    def front(self):
        return self.heap[0]
