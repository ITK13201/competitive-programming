# Bellman–Ford_algorithm.py - 単一始点最短経路問題1(ベルマンフォード法)

inf = float('inf')

class edge:
    def __init__(self, from_: int, to: int, cost: int):
        # 辺の始点
        self.from_ = from_
        # 辺の終点
        self.to = to
        # 辺のコスト
        self.cost = cost


n, w = map(int, input().split())
es = []
for i in range(w):
    x, y, z = map(int, input().split())
    add1 = edge(x, y, z)
    add2 = edge(y, x, z)
    es.append(add1)
    es.append(add2)


'''input
7 10
0 1 2
0 2 5
1 2 4
1 3 6
1 4 10
2 3 2
3 5 1
4 5 3
4 6 5
5 6 9
'''

# s番目の頂点から各頂点への最短距離を求める
def shortest_path(s):
    # 最短距離
    d = [inf for i in range(n)]
    d[s] = 0
    while True:
        update = False
        for i in range(w*2):
            e = es[i]
            if d[e.from_] != inf and d[e.to] > d[e.from_] + e.cost:
                d[e.to] = d[e.from_] + e.cost
                update = True
        
        if not update:
            break
    
    return d

print(shortest_path(0))