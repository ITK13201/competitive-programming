from fractions import *

def lcm(x, y):
    z = x * y / gcd(x, y)
    return z

A, B = map(int, input().split())

ans = int(lcm(A, B))
print(ans)
