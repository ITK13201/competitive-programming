n = int(input())

def popcount(x):
    return bin(x).count('1')

g = [[-1 for j in range(n)] for i in range(n)]

for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        x -= 1
        g[i][x] = y

ans = 0
for i in range(1 << n):
    d = [0 for _ in range(n)]
    for j in range(n):
        if i >> j & 1:
            d[j] = 1
    ok = True
    for j in range(n):
        if d[j]:
            for k in range(n):
                if g[j][k] == -1:
                    continue
                if g[j][k] != d[k]:
                    ok = False
    if ok:
        ans = max(ans, popcount(i))

print(ans)