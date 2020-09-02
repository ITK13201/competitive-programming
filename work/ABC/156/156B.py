N, K = map(int, input().split())

a = []
i = 0
while N > 0:
    a.append(N % K)
    N = N // K
    i += 1

ans = ''
while i > 0:
    ans += str(a[i - 1])
    i -= 1

ansl = len(ans)

print(ansl)