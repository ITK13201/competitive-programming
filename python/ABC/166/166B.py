import sys
from math import floor,ceil,sqrt,factorial,log
from heapq import heapify, heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from decimal import Decimal
inf = float('inf')
MOD = 1000000007

n, k = map(int, input().split())
d = []
A = []
for i in range(k):
    x = int(input())
    d.append(x)
    y = list(map(int, input().split()))
    A.append(y)


s = [0 for _ in range(n)]

for i in range(k):
    for j in range(d[i]):
        s[A[i][j]-1] += 1

ans = 0
for i in range(n):
    if s[i] == 0:
        ans += 1

print(ans)
