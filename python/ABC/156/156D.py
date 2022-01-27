from math import *
from scipy.special import comb

def comb(N, r):
    return factorial(N) // factorial(r) // factorial(N - r)

n, a, b = map(int, input().split())

mod = 1e+9 + 7

sum = 0

sum = int(2 ** n) - 1

print(sum)

sub_a = comb(n, a)
sub_b = comb(n, b)

print(sub_a, sub_b)
sum -= sub_a + sub_b

print(sum)

ans = int(sum % mod)

print(ans)