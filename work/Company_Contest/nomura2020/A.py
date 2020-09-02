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

h1, m1, h2, m2, k = map(int, input().split())

t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

if t2 > t1:
    ans = t2 - t1 - k
    if ans < 0:
        ans = 0
    print(ans)
else:
    ans = 24 - t1 + t1
    if ans < 0:
        ans = 0
    print(ans)