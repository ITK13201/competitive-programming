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

a, b = input().split()

a = int(a)
b = list(b)
for i in range(len(b)):
    if b[i] == '.':
        pos = i

x = len(b) - pos - 1
b.pop(pos)
b = int(''.join(b))

ans = a * b
ans = str(ans)
if len(ans) < 2:
    ans = int(int(ans) * 10**(-2))
else:
    ans = int(ans[:-pos -1])

print(ans)


