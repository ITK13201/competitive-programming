# LCS.py - 最長共通部分列問題 (Longest-common subsequence problem)

n = int(input())
m = int(input())
s = input()
t = input()

'''input
4
4
abcd
becd
'''

'''
dp[i + 1][j + 1] = 
    max(dp[i][j] + 1, dp[i][j + 1], dp[i + 1][j])   ( = dp[i][j] + 1) (s[i + 1] = t[j + 1])
    max(dp[i][j + 1], dp[i + 1][j]) (それ以外)

'''

dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[n][m])