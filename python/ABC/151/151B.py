from numpy import *

n, k, m = map(int, input().split())

A = zeros(n-1)
A = list(map(int, input().split()))

sum = 0
for i in range(n-1):
    sum += A[i]

for i in range(k+1):
    x = sum + i
    ave = x / n
    if ave >= m:
        ans = i
        break
    else:
         ans = -1

print(ans)