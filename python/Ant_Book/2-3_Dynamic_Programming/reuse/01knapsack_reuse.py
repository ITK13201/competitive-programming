# 01knapsack_reuse.py - 01ナップザック問題

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

# 初期化
dp = [0 for j in range(W + 1)]

for i in range(n):
    j = W
    while w[i] <= j:
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])
        j -= 1

print(dp[W])