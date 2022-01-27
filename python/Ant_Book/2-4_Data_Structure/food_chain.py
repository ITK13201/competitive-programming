class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    # 木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            return self.find(self.par[x])
    
    # xとyに属する集合を併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

N, K = map(int, input().split())
T, X, Y = [], [], []
for i in range(K):
    tt, xx, yy = map(int, input().split())
    T.append(tt)
    X.append(xx)
    Y.append(yy)

'''input
100 7
1 101 1
2 1 2
2 2 3
2 3 3
1 1 3
2 3 1
1 5 5
'''

# union_find木を初期化
# x, x + N, x + 2 * N をx-A, x-B, x-C の要素とする
uf = UnionFind(N * 3)

ans = 0
for i in range(K):
    t = T[i]
    x = X[i] - 1
    y = Y[i] - 1

    # 正しくない番号
    if x < 0 or N <= x or y < 0 or N <= y:
        ans += 1
        continue

    if t == 1:
        # xとyは同じ種類という情報
        if uf.same(x, y + N) or uf.same(x, y + 2 * N):
            ans += 1
        else:
            uf.unite(x, y)
            uf.unite(x + N, y + N)
            uf.unite(x + N * 2, y + N * 2)
    else:
        # xはyを食べるという情報
        if uf.same(x, y) or uf.same(x, y + 2 * N):
            ans += 1
        else:
            uf.unite(x, y + N)
            uf.unite(x + N, y + 2 * N)
            uf.unite(x + 2 * N, y)
    

print(ans)

