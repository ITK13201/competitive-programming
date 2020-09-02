def ok(n, k, a, x):
    total = 0
    for i in range(n):
        if a[i] < 0:
            l = -1
            r = n
            while l + 1 < r:
                m = (l + r) // 2
                if a[m] * a[i] < x:
                    r = m
                else:
                    l = m
            total += n - r
        else:
            l = -1
            r = n
            while l + 1 < r:
                m = (l + r) // 2
                if a[m] * a[i] < x:
                    l = m
                else:
                    r = m
            total += r
        
        if a[i] * a[i] < x:
            total -= 1
    total //= 2
    return total < k


N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

INF = int(1e+18) + 1
l = -INF
r = INF
while l + 1 < r:
    x = (l + r) // 2
    if ok(N, K, A, x):
        l = x
    else:
        r = x

print(l)


