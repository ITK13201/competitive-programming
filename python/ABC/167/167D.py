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

class Queue:
    # value: list
    def __init__(self, value: list):
        self.value = deque(value)
    
    def push(self, item):
        self.value.append(item)
    
    def pop(self):
        return self.value.popleft()
    
    def pushpop(self, item):
        self.value.append(item)
        return self.value.popleft()
    
    def __call__(self):
        return self.value
    
    def __len__(self):
        return len(self.value)
    
    def size(self):
        return len(self.value)
    
    def empty(self):
        return len(self.value) == 0
    
    def front(self):
        return self.value[0]
    
    def back(self):
        return self.value(-1)
    
    def sorted(self):
        return deque(sorted(self.value))



n, k = map(int, input().split())
a = list(map(int, input().split()))

s = [0 for _ in range(n)]
t = []
q = Queue([a[0] - 1])
f1, f2 = inf, inf
for i in range(k):
    r = q.pop()
    q.push(a[r] - 1)
    s[q.front()] += 1
    if s[q.front()] == 2:
        f1 = i
    if 2 <= s[q.front()] < 3:
        t.append(q.front())
    if s[q.front()] == 3:
        f2 = i
        break
    
if f1 == inf:
    print(q.front())
    exit()
if f2 == inf:
    print(q.front())
    exit()
if f1 != inf and f2 != inf:
    g = k - f1 + 1
    e = g // (f2 - f1 + 1)
    ans = f1 + e*(f2 - f1)
    anss = k - ans
    print(t[anss])