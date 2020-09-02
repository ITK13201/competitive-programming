n, w = map(int, input().split())    # n: 頂点の数, w: 辺の数
g = [[] for i in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)