L = int(input())
n = int(input())
x = list(map(int, input().split()))

# 最小の時間
minT = 0
for i in range(n):
    minT = max(minT, min(x[i], L - x[i]))

# 最大の時間
maxT = 0
for i in range(n):
    maxT = max(maxT, max(x[i], L - x[i]))


print(minT, maxT)