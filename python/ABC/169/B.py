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

n = int(input())
a = list(map(int, input().split()))

ans = 1
flag = True
for i in range(len(a)):
    if a[i] == 0:
        print(0)
        exit()

for i in range(n):
    ans *= a[i]
    if ans > 1e+18:
        flag = False
        break;

if(flag):
    print(ans)
else:
    print(-1)