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

def souu(z):
    for i in range(z // 2):
        if z % (2 * i + 1)!= 0:
            k = 2
            while z > 0:
                if (2 * i + 1) ** k == z:
                    return True
            k += 1
    return False

n = int(input())
arr = []
z = 0
cnt = 0
while True:
    for i in range(n // 2):
        if n % (2 * i + 1) == 0:
            z = 2 * i + 1
        if i == n // 2:
            break

    if souu(z):
        if z in arr:
            break
        else:
            cnt += 1
            arr.append(z)
            n = n // z
    else:
        continue


print(cnt)



    