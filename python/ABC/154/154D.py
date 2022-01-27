from numpy import *

N, K = map(int, input().split())
p = list(map(int, input().split()))
q = zeros(K, dtype=int)

s = 0
for i in range(N - K + 1):
    t = 0
    for j in range(i, i + K):
        t += p[j]
    if s < t:
        s = t
        r = 0
        for j in range(i, i + K):
            q[r] = p[j]
            r += 1

pointc = []
for i in range(K):
    point = 0
    for j in range(0, q[i]):
        point += j + 1
    
    pointc.append(point / q[i])

print(sum(pointc))
    
