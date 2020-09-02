import sys
from math import floor,ceil,sqrt,factorial,log
from heapq import heapify, heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from decimal import Decimal
inf = float('inf')
MOD = 1000000007


n, m = map(int, input().split())
h = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    x,y = map(int, input().split())
    g[y-1].append(x-1)
    g[x-1].append(y-1)


def dfs(v):
    for i in range(len(g[v])):
        if h[g[v][i]] >= h[v]:
            return False
    
    return True


ans = 0
for i in range(n):
    if dfs(i):
        ans += 1

print(ans)