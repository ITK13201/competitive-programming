from numpy import *

N = int(input())
a = zeros(N)
a = list(map(int, input().split()))

count = 0

for i in range(N):
    if count + 1 == a[i]:
        count += 1

ans = N - count

if count == 0:
    ans = -1

print(ans)
