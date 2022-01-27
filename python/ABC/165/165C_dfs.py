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

arr = []
def dfs(A: list):
    if len(A) == n:
        arr.append(A)
        return
    
    if len(A) == 0:
        s = 1
    else:
        s = A[-1]
    
    while s <= m:
        dfs(A + [s])
        s += 1
       

def main():
    dfs([])
    ans = 0
    for A in arr:
        tmp = 0
        for a,b,c,d in abcd:
            if A[b-1] - A[a-1] == c:
                tmp += d
        ans = max(ans, tmp)
    
    print(ans)

if __name__ == "__main__":
    main()
