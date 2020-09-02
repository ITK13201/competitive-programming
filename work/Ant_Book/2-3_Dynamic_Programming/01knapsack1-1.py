# 01knapsack1-1.py - 01ナップザック問題

n = int(input())
W = int(input())
w = []
v = []
for _ in range(n):
    ww, vv = map(int, input().split())
    w.append(ww)
    v.append(vv)

'''input
4
5
2 3
1 2
3 4
2 2
'''

# i番目以降の品物から重さの総和がj以下となるように選ぶ
def rec(i, j):
    if i == n:
        # もう品物は残っていない
        res = 0
    elif j < w[i]:
        # この品物は入らない
        res = rec(i + 1, j)
    else:
        # 入れない場合と入れる場合を両方試す
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])
    
    return res

print(rec(0, W))