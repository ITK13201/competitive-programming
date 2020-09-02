import sys
input = lambda: sys.stdin.readline().rstrip()
from math import floor,ceil,sqrt,factorial,log
from heapq import heapify, heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from decimal import Decimal
inf = float('inf')
mod = 1000000007


n, m, x = map(int, input().split())
c = []
a = []
for i in range(n):
    y = list(map(int, input().split()))
    c.append(y[0])
    a.append(y[1:])

dp = [[inf for j in range(x + 1)] for i in range(n + 1)]
dp[0][0] = 0

ans = 0
for i in range(n):
    for j in range(x + 1):
        if j < a[i][j]:
            dp[i + 1][j] = dp[i][0]
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - a[i][j]] + c[i])

print(dp[n][x])