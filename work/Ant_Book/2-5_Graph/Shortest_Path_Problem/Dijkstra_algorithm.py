# Dijkstra_algorithm.py - 単一始点最短経路問題（ダイクストラ法）

inf = float('inf')

n, w = map(int, input().split())
cost = [[inf for j in range(w)] for i in range(n)]
for i in range(w):
    x, y, z = map(int, input().split())
    cost[x][y] = z
    cost[y][x] = z

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
    d = [inf for _ in range(n)]
    used = [False for _ in range(n)]
    d[s] = 0

    while True:
        v = -1
        # まだ使われていない頂点の中から距離が最小のものを探す
        for i in range(n):
            if not used[i] and (v == -1 or d[i] < d[v]):
                v = i
        
        if v == -1:
            break

        used[v] = True

        for i in range(n):
            d[i] = min(d[i], d[v] + cost[v][i])
    
    return d


print(dijkstra(0))