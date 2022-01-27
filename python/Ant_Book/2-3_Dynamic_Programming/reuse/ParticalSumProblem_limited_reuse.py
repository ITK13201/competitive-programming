# ParticalSumProbrem_limited_reuse.py - 個数制限付き部分和問題　再利用編

n = int(input())
K = int(input())
a = list(map(int, input().split()))
m = list(map(int, input().split()))

'''input
3
17
3 5 7
3 2 2
'''

'''
dp[i + 1][j]: i番目まででjを作る際に余る最大のi番目の個数 (作れない場合は-1)
dp[i + 1][j] = 
    m[i]                        (dp[i][j] >= 0)
    -1                          (j < a[i] or dp[i + 1][j - a[i] <= 0)
    dp[i + 1][j - a[i]] - 1     (それ以外)
'''

dp = [[-1 for j in range(K + 1)] for i in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(K + 1):
        if dp[i][j] >= 0:
            dp[i + 1][j] = m[i]
        elif j < a[i] or dp[i + 1][j - a[i]] <= 0:
            dp[i + 1][j] = -1
        else:
            dp[i + 1][j] = dp[i + 1][j - a[i]] - 1

if dp[n][K] >= 0:
    print('Yes')
else:
    print('No')


# dp = [-1 for j in range(K + 1)]
# dp[0] = 0

# for i in range(n):
#     for j in range(K + 1):
#         # i-1 番目までで余りが0以上(jが作れる)のとき，m[i]個残せる
#         if dp[j] >= 0:
#             dp[j] = m[i]
#         # jが作れないとき
#         elif j < a[i] or dp[j - a[i]] <= 0:
#             dp[j] = -1
#         # i番目まででj - a[i]を作る際にi番目をk(>0)個残せるならばi番目をi-1個残してjを作ることができる
#         else:
#             dp[j] = dp[j - a[i]] - 1

# if dp[K] >= 0:
#     print('Yes')
# else:
#     print('No')
