import sys
input = lambda: sys.stdin.readline().rstrip()
from math import floor,ceil,sqrt,factorial,log, sin, cos, fabs, pi
from heapq import heapify, heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from decimal import Decimal
inf = float('inf')
mod = 1000000007

a, b, h, m = map(int, input().split())

longt = 6
mint = 1 / 2

time = h * 60 + m

longtt = longt * time % 360
mintt = mint * time % 360

w = fabs(longtt - mintt)

if w > 180:
    w = 360 - w

w = w / 180 * pi
l = sqrt(a**2 + b**2 - 2 * a * b * cos(w))
print(l)

