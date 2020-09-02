a, b, c, d = map(int, input().split())

while a > 0 or c > 0:
    c -= b
    if c <= 0:
        break
    a -= d

if a <= 0:
    print('No')
elif c <= 0:
    print('Yes')