from math import *

N = int(input())
X = list(map(int, input().split()))

sum = 0
for i in range(len(X)):
    sum += X[i]

ave = int(round(sum / len(X), 0))

ans = 0
for i in range(len(X)):
    ans += int(pow(X[i] - ave, 2))

print(ans)