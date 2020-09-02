N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)

ans = 0
for i in range(N):
    tmp = total * (1 / (4 * M))
    if A[i] >= tmp:
        ans += 1

if ans >= M:
    print('Yes')
else:
    print('No')