INF = 10**9

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

# (i, j)に進むときの色の反転回数の最小値
dp = [[INF for j in range(W)] for i in range(H)]

if s[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(H):
    for j in range(W):
        if i == H - 1 and j == W - 1:
            break
        
        if i != H - 1:
            if s[i][j] == '.' and s[i + 1][j] == '#':
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
        
        if j != W - 1:
            if s[i][j] == '.' and s[i][j + 1] == '#':
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            else:
                dp[i][j + 1] = min(dp[i][j], dp[i][j + 1])

print(dp[H-1][W-1])