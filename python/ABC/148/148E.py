n = int(input())

def g1(n, p):
    if n == 0:
        return 0
    else:
        return n // p + g1(n // p, p)

def g2(n, p):
    res = 0
    if n % 2 == 1:
        return g1(n, p) - g2(n - 1, p)
    else:
        res = g1(n // 2, p)
        if p == 2:
            res += n // 2
        return res


ans = min(g2(n, 2), g2(n, 5))
print(ans)