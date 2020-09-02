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

n = int(input()) - 1

alpha = list('abcdefghijklmnopqrstuvwxyz')

if 0 <= n <= 25:
    tmp = 0
    res = list(product(alpha, repeat=1))
elif 26 <= n <= 701:
    tmp = 26
    res = list(product(alpha, repeat=2))
elif 702 <= n <= 18277:
    tmp = 702
    res = list(product(alpha, repeat=3))
elif 18278 <= n <= 475253:
    tmp = 18278
    res = list(product(alpha, repeat=4))
elif 475254 <= n <= 12356629:
    tmp = 475254
    res = list(product(alpha, repeat=5))
elif 12356630 <= n <= 321272405:
    tmp = 12356630
    res = list(product(alpha, repeat=6))
elif 321272406 <= n <= 8353082581:
    tmp = 321272406
    res = list(product(alpha, repeat=7))
elif 8353082581 <= n <= 217180147157:
    tmp = 8353082581
    res = list(product(alpha, repeat=8))
elif 217180147158 <= n <= 5646683826133:
    tmp = 217180147158
    res = list(product(alpha, repeat=9))

print(res[n-tmp])
