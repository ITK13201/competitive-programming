from decimal import Decimal

a, b, c = map(int, input().split())

a = Decimal(str(a)).sqrt()
b = Decimal(str(b)).sqrt()
c = Decimal(str(c)).sqrt()

if a + b < c:
    print('Yes')
else:
    print('No')