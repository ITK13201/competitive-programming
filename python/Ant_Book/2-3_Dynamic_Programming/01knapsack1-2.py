# 01knapsack1-2.py - 01ナップザック問題 改良版

INF = 10**9

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

# # 初期化
# dp = [[-INF for j in range(W + 1)] for i in range(n + 1)]

# def rec(i, j):
#     if dp[i][j] >= 0:
#         # すでに調べたことがあるならばその結果を再利用
#         return dp[i][j]
    
#     if i == n:
#         res = 0
#     elif j < w[i]:
#         res = rec(i + 1, j)
#     else:
#         res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])
    
#     # 結果をテーブルに記憶する
#     dp[i][j] = res

#     return res

# print(rec(0, W))


# # 初期化
# dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

# for i in reversed(range(n)):
#     for j in range(W + 1):
#         if j < w[i]:
#             dp[i][j] = dp[i + 1][j]
#         else:
#             dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])

# print(dp[0][W])


# 初期化
dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

for i in range(n):
    for j in range(W + 1):
        if j < w[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])

print(dp[n][W])




