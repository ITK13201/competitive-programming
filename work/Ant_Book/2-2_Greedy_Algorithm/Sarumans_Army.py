# Sarumans_Army.py - Saruman's Army (POJ)

N = int(input())
R = int(input())
X = list(map(int, input().split()))

'''input
6
10
1 7 15 20 30 50
'''

X.sort()

i = 0
ans = 0
while i < N:
    # s はカバーされていない一番左の点の位置
    s = X[i]
    i += 1
    # s から距離 R を超える点まで進む
    while i < N and X[i] <= s + R:
        i += 1
    
    # p は新しく点をつける位置
    p = X[i - 1]
    # p から距離 R を超える点まで進む
    while i < N and X[i] <= p + R:
        i += 1
    
    ans += 1

print(ans)

