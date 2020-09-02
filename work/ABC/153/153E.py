INF = float('inf')

H, N = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


# i個目までを使って与えた魔力の総和がjの時の最小コスト
dp = [[INF for j in range(H + 1)] for i in range(N + 1)]

dp[0][0] = 0

for i in range(N):
    for j in range(H + 1):
        if j < A[i]:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][0] + B[i])
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - A[i]] + B[i])

print(dp[N][H])
