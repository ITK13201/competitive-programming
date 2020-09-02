N = int(input())
A = list(map(int, input().split()))

# dp[i + 1][j + 1] : i番目をj番目に移動させた時の最大のうれしさ
dp = [[-1 for j in range(N + 1)] for i in range(N + 1)]


