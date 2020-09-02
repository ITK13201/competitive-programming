k = int(input())
a, b = map(int, input().split())

s = 0
i = 0
while True:
    if s >= a:
        break
    s = k * i
    i += 1

if a <= s <= b:
    print('OK')
else:
    print('NG')