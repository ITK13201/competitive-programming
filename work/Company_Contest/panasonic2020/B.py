H, W = map(int, input().split())

HW = H * W
HW2 = HW // 2

if H == 1 or W == 1:
    ans = 1
else:
    if HW % 2 == 0:
        ans = HW2
    else:
        ans = HW2 + 1

print(ans)