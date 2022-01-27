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
            return False
        
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            return True
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            return True
    
    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m, k = map(int, input().split())
fl = [0 for i in range(n)]
bl = [0 for i in range(n)]
uf = UnionFind(n)

# 友達関係
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    fl[a] += 1
    fl[b] += 1
    uf.unite(a, b)

# ブロック関係
for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.find(c) == uf.find(d):
        bl[c] += 1
        bl[d] += 1
    


ans = [uf.rank[i] - fl[i] - bl[i] - 1 for i in range(n)]

print(*ans)
