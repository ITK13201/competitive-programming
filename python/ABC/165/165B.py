from decimal import Decimal

x = int(input())

s = 100
r = 0.01
i = 0
ans = 0
while not(s >= x):
    s = int(s * (1 + r))
    ans = i
    i += 1

print(ans + 1)