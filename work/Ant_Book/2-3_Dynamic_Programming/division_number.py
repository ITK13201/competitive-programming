# division_number.py - 分割数

n = int(input())
m = int(input())
M = int(input())

'''input
4
3
10000
'''

'''
dp[i][j]: jのi分割の総数
dp[i][j] = dp[i][j - i] + dp[i - 1][j]
'''

dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

dp[0][0] = 1

for i in range(1, m + 1):
    for j in range(n + 1):
        if j - i >= 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j - i] % M
        else:
            dp[i][j] = dp[i - 1][j];


print(dp[m][n])