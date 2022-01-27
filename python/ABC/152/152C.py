from numpy import *

N = int(input())
P = list(map(int, input().split()))

l = zeros(N+1, dtype=int)

l[0] = P[0]
j = 0
for i in range(1, N):
    if P[i] < l[j]:
        l[j+1] = P[i]
        j += 1
    else:
        pass


count = 0
for i in range(N):
    if l[i] == 0:
        break
    count += 1

print(count)
