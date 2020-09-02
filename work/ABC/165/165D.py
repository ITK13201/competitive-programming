import math

a, b, n = map(int, input().split())
x = b - 1
if n < x:
    x = n

ans = int(a * x / b) - a * int(x / b)

print(ans)