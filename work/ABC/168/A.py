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

n = list(input())

if n[-1] == '2' or n[-1] == '4' or n[-1] == '5' or n[-1] == '7' or n[-1] == '9':
    print('hon')
elif n[-1] == '0' or n[-1] == '1' or n[-1] == '6' or n[-1] == '8':
    print('pon')
elif n[-1] == '3':
    print('bon')