# knapsack_unlimited2 - 個数制限なしナップザック問題

n = int(input())
W = int(input())
w = []
v = []
for _ in range(n):
    ww, vv = map(int, input().split())
    w.append(ww)
    v.append(vv)

'''input
3
7
3 4
4 5
2 3
'''

'''
dp[0][j] = 0
dp[i + 1][j] = max(dp[i][j - k*w[i]] + k*v[i]) (0 <= k)
'''

# 初期化
dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

for i in range(n):
    for j in range(W + 1):
        if j < w[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])

print(dp[n][W])


# for i in range(n + 1):
#     for j in range(W + 1):
#         print(dp[i][j], end=', ')
#     print()
