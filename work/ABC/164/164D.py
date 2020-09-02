s = input()
n = len(s)

ans = 0
x2019 = 2019
i = 2
while x2019 < int(s):
    if str(x2019) in s:
        ans += 1
    x2019 = 2019 * i
    i += 1

print(ans)