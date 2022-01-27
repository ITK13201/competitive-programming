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
        if len(self.heap) == 0:
            return True
        else:
            return False

N, L, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

'''input
4 25 10
10 14 20 21
10 5 2 4
'''

# 簡単のため，ゴールをガソリンスタンドに追加
A.append(L)
B.append(0)
N += 1

# ガソリンスタンドを管理するキュー
que = PriorityQueue_max([])

'''
@param ans: 補給回数
@param pos: 今いる場所
@param tank: タンクのガソリンの量
'''
ans = 0
pos = 0
tank = P

for i in range(N):
    # 次に進む距離
    d = A[i] - pos

    # 十分な量になるまでガソリンを補給
    while tank - d < 0:
        if que.empty():
            print('-1')
            exit()
        tank += que.pop()
        ans += 1
    
    tank -= d
    pos = A[i]
    que.push(B[i])


print(ans)