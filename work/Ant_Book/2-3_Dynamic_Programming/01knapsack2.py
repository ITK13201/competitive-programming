# 01knapsack2.py - 01ナップザック問題 その2

INF = 10**9
MAX_N = 100
MAX_V = 100

n = int(input())
W = int(input())
w = []
v = []
for _ in range(n):
    ww, vv = map(int, input().split())
    w.append(ww)
    v.append(vv)

'''input
4
5
2 3
1 2
3 4
2 2
'''

'''
dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
'''

dp = [[INF for j in range(n * max(v) + 1)] for i in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n * max(v) + 1):
        if j < v[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])

res = 0
for i in range(n * max(v) + 1):
    if dp[n][i] <= W:
        res = i

print(res)