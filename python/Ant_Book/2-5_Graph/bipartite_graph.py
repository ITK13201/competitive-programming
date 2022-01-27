# bipertite_graph.py - 二部グラフ判定

n, w = map(int, input().split())    # n: 頂点の数, w: 辺の数
g = [[] for i in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
color = [0 for _ in range(n)]

'''input1
3 3
0 1
1 2
2 0
'''
'''input2
4 4
0 1
1 2
2 3
3 0
'''

# 頂点を1と-1で塗っていく
def dfs(v, c):
    # 頂点vをcで塗る
    color[v] = c
    for i in range(len(g[v])):
        # 隣接している頂点が同じ色ならfalse
        if color[g[v][i]] == c:
            return False
        # 隣接している頂点がまだ塗られていないなら-cで塗る
        if color[g[v][i]] == 0 and not dfs(g[v][i], -c):
            return False
    
    # 全ての頂点が塗れたらtrue
    return True


for i in range(n):
    if color[i] == 0:
        # まだ頂点が塗られていなければ1で塗る
        if not dfs(i, 1):
            print('No')
            exit()


print('Yes')