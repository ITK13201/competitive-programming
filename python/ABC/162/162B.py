N = int(input())

l = []
for i in range(N):
    x = i + 1
    if x % 3 != 0 and x % 5 != 0:
        l.append(x)

ans = sum(l)
print(ans)