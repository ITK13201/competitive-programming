import sys
input = sys.stdin.readline
from math import floor,ceil,sqrt,factorial,log
from heapq import heapify, heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from decimal import Decimal
inf = float('inf')
MOD = 1000000007
def INT_(n): return int(n) - 1
def MI(): return map(int, input().split())
def MF(): return map(float, input().split())
def MI_(): return map(INT_,input().split())
def LI(): return list(MI())
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return list(MF())
def LIN(n: int): return [I() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]
def LLIN_(n: int): return [LI_() for _ in range(n)]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def I(): return int(input())
def F(): return float(input())
def ST(): return input().replace('\n', '')

n, m, q = MI()
abcd = LLIN(q)

ans = 0
num = [0 for _ in range(10)]
for i0 in range(1, m+1):
    num[0] = i0
    for i1 in range(i0, m+1):
        num[1] = i1
        for i2 in range(i1, m+1):
            num[2] = i2
            for i3 in range(i2, m+1):
                num[3] = i3
                for i4 in range(i3, m+1):
                    num[4] = i4
                    for i5 in range(i4, m+1):
                        num[5] = i5
                        for i6 in range(i5, m+1):
                            num[6] = i6
                            for i7 in range(i6, m+1):
                                num[7] = i7
                                for i8 in range(i7, m+1):
                                    num[8] = i8
                                    for i9 in range(i8, m+1):
                                        num[9] = i9
                                        tmp = 0
                                        for a,b,c,d in abcd:
                                            if num[b-1] - num[a-1] == c:
                                                tmp += d
                                        ans = max(ans, tmp)

print(ans)