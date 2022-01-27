import numpy as np

N, M = map(int, input().split())
s = []
c = []
for i in range(M):
    x, y = map(int, input().split())
    s.append(x)
    c.append(y)

t = ''
if N in s:
    for i in range(N):
        if N - i - 1 in s:
            t
else:
    print('-1')

