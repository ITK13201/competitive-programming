# knapsack_unlimited1 - 個数制限なしナップザック問題

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
        k = 0
        while k * w[i] <= j:
            # max(dp[i][j - k * w[i] + k * v[i]]  (0 <= k))
            # k をループする中で自分(dp[i + 1][j])と比較している
            # k = 0 の時が1つも入れない0個の場合，while で制限をかけているので，j を超すことはない
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - k * w[i]] + k * v[i])
            k += 1

print(dp[n][W])

# for i in range(n + 1):
#     for j in range(W + 1):
#         print(dp[i][j], end=', ')
#     print()









