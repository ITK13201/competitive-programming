import sys
from math import floor,ceil,sqrt,factorial,log
from heapq import heapify, heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from decimal import Decimal
inf = float('inf')
MOD = 1000000007


n = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        nl = abs(i - j)
        h = A[i] + A[j]
        if nl == h:
            ans += 1

print(ans)