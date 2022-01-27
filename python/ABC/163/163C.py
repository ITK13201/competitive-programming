N = int(input())
A = list(map(int, input().split()))

ans = [0 for i in range(N)]

for i in range(N - 1):
    ans[A[i] - 1] += 1

[print(ans[i]) for i in range(len(ans))]