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
