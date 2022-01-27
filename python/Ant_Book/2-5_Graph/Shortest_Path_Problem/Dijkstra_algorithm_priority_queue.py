# Dijkstra_algorithm_priority_queue.py - 単一始点最短経路問題（ダイクストラ法） priority queueを用いた実装

inf = float('inf')

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


class edge:
    def __init__(self, to: int, cost: int):
        self.to = to
        self.cost = cost
        

n, w = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(w):
    x, y, z = map(int, input().split())
    g[x].append(edge(y, z))
    g[y].append(edge(x, z))

# cost[u][v]: 辺uvのコスト


'''input
7 10
0 1 2
0 2 5
1 2 4
2 3 2
1 3 6
1 4 10
3 5 1
4 5 3
4 6 5
5 6 9
'''

def dijkstra(s):
    que = PriorityQueue()
    d = [inf for _ in range(n)]
    d[s] = 0
    que.push([0, s])

    while not que.empty():
        p_first, p_second = que.pop()
        v = p_second
        if d[v] < p_first:
            continue
        for i in range(len(g[v])):
            e = g[v][i]
            if d[e.to] > d[v] + e.cost:
                d[e.to] = d[v] + e.cost
                que.push([d[e.to], e.to])
    
    return d


print(dijkstra(0))