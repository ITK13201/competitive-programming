a, b = map(int, input().split())

la = ''
lb = ''

for i in range(b):
    la += str(a)

for i in range(a):
    lb += str(b)

if a <= b:
    print(la)
else:
    print(lb)

