# Bellman–Ford_algorithm_negative.py - 単一始点最短経路問題1(ベルマンフォード法)[負のコストの経路が存在する場合]

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
    x,y,z = map(int, input().split())
    add1 = edge(x,y,z)
    add2 = edge(y,x,z)
    es.append(add1)
    es.append(add2)
# 最短距離
d = [inf for _ in range(n)]


'''input
7 10
0 1 2
0 2 5
1 2 4
2 3 2
1 3 6
1 4 -11
3 5 1
4 5 3
4 6 5
5 6 9
'''

# 負の経路が存在するならば，true
def find_negative_loop():
    d[0] = 0
    # この場合は始点はどこでもよい
    for i in range(n):
        for j in range(w*2):
            e = es[j]
            if d[e.to] > d[e.from_] + e.cost:
                d[e.to] = d[e.from_] + e.cost
                # n回目にも更新があるなら負の回路が存在する
                if i == n - 1:
                    return True
    
    return False


print(find_negative_loop())

