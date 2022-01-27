import math

a, b, c = map(int, input().split())

# a + b + 2 sqrt(ab) < c
# c - a - b > 2 sqrt(ab)
# (c - a - b)^2 > 4ab

if (c - a - b)**2 > 4 * a * b and c - a - b > 0:
    print('Yes')
else:
    print('No')