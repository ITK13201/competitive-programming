# Fence_Repair.py - Fence Repair (POJ)

N = int(input())
L = list(map(int, input().split()))

'''input
3
8 5 8
'''

ans = 0
while N > 1:
    # 一番短い板mii1, 次に短い板mii2を求める
    mii1 = 0
    mii2 = 1
    if L[mii1] > L[mii2]:
        mii1, mii2 = mii2, mii1
    
    for i in range(2, N):
        if L[i] < L[mii1]:
            mii2 = mii1
            mii1 = i
        elif L[i] < L[mii2]:
            mii2 = i

    # それらを統合
    t = L[mii1] + L[mii2]
    ans += t

    if mii1 == N - 1:
        mii1, mii2 = mii2, mii1
    L[mii1] = t
    # for 文の探索範囲が (2, N) なので，'N -= 1' したときに，mii2に割り当てないとL[N-1]がなかったことになる．
    L[mii2] = L[N - 1]
    N -= 1

print(ans)