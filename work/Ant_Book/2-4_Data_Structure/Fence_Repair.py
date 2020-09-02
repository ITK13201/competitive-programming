# Fence_Repair.py - Fence Repair (PKU) のpriority queue 版

import heapq

class PriorityQueue:
    # heap: list
    def __init__(self, heap = []):
        self.heap = heap
        heapq.heapify(self.heap)
    
    def push(self, item):
        heapq.heappush(self.heap, item)
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def pushpop(self, item):
        return heapq.heappop(self.heap, item)
    
    def __call__(self):
        return self.heap
    
    def __len__(self):
        return len(self.heap)
    
    def empty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False
    
    def front(self):
        return self.heap[0]


N = int(input())
L = list(map(int, input().split()))

'''input
3
8 5 8
'''

ans = 0
que = PriorityQueue([])

for i in range(N):
    que.push(L[i])

while len(que) > 1:
    l1 = que.pop()
    l2 = que.pop()

    ans += l1 + l2
    que.push(l1 + l2)

print(ans)