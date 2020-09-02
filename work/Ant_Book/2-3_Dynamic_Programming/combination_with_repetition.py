# combination_with_repetition.py - 重複組み合わせ (Combinaton with Repetition)

n = int(input())
m = int(input())
a = list(map(int, input().split()))
M = int(input())

'''input
3
3
1 2 3
10000
'''

'''
dp[i + 1][j] = dp[i][j - k] (0 <= k <= min(j, a[i]))
=>  dp[i + 1][j] = dp[i + 1][j - 1 - k] + dp[i][j] - dp[i][j - 1 - a[i]] (0 <= k <= min(j - 1, a[i]))
'''

dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

# 一つも選ばない方法は常に一通り
for i in range(n + 1):
    dp[i][0] = 1

for i in range(n):
    for j in range(1, m + 1):
        if j - 1 - a[i] >= 0:
            # 引き算が含まれる場合には負の数が含まれないように注意する
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j] - dp[i][j - 1 - a[i]] + M) % M
        else:
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % M

print(dp[n][m])