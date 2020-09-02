A = int(input())
B = int(input())

if A == 1:
    if B == 2:
        ans = 3
    if B == 3:
        ans = 2
elif A == 2:
    if B == 1:
        ans = 3
    if B == 3:
        ans = 1
elif A == 3:
    if B == 1:
        ans = 2
    if B == 2:
        ans = 1

print(ans)