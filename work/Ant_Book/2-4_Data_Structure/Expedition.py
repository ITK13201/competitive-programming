# Expedition.py - Expedition (POJ)

import heapq

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
que = []
heapq.heapify(que)

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
        if len(que) == 0:
            print('-1')
            exit()
        tank += (-1) * heapq.heappop(que)
        ans += 1
        print(que, 111)
    
    tank -= d
    pos = A[i]
    heapq.heappush(que, B[i] * (-1))
    print(que, 222)


print(ans)