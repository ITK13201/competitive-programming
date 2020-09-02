# knapsack_unlimited_reuse - 個数制限なしナップザック問題

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

dp = [0 for j in range(W + 1)]

for i in range(n):
    j = w[i]
    while j <= W:
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])
        j += 1

print(dp[W])