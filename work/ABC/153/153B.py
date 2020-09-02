from numpy import *

H, N = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += A[i]

if H - sum <= 0:
    print('Yes')
else:
    print('No')