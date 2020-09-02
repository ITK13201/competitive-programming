# ParticalSumProblem_limited.py - 個数制限付き部分和問題

n = int(input())
K = int(input())
a = list(map(int, input().split()))
m = list(map(int, input().split()))

'''input
3
17
3 5 7
3 2 2
'''

'''
dp[i + 1][j]: i番目まででjが作れるか
'''

dp = [[False for j in range(K + 1)] for i in range(n + 1)]

dp[0][0] = True
for i in range(n):
    for j in range(K + 1):
        k = 0
        while k <= m[i] and k * a[i] <= j:
            dp[i + 1][j] |= dp[i][j - k * a[i]]
            k += 1

if dp[n][K]:
    print('Yes')
else:
    print('No')