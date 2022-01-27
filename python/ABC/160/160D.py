import sys

input = sys.stdin.readline

N, X, Y = map(int, input().split())
X -= 1
Y -= 1

ans = [0 for _ in range(N - 1)]

for i in range(N - 1):
    for j in range(i + 1, N):
        d1 = abs(j - i)
        d2 = abs(X - i) + 1 + abs(j - Y)
        ans[min(d1, d2) - 1] += 1

[print(ans[i]) for i in range(N - 1)]
