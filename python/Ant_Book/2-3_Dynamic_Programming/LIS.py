# LIS.py - 最長増加部分列問題(Longest Increasing Subsequence)

INF = 10**9

import bisect

n = int(input())
a = list(map(int, input().split()))

'''input
5
4 2 3 1 5
'''

'''
dp[i]: 最後がa[i]であるような最長の部分増加列の長さ
dp[i] = max(1, dp[j] + 1) (j < i and a[j] < a[i])
'''

# dp = [0 for i in range(n + 1)]
# dp[0] = 0

# for i in range(n):
#     dp[i + 1] = 1
#     j = 0
#     while j < i:
#         if a[j] < a[i]:
#             dp[i + 1] = max(dp[i + 1], dp[j] + 1)
#         j += 1

# print(dp[n])


'''
dp[i]: 長さがi + 1であるような増加部分列における最終要素の最小値（存在しない場合はINF）
dp[i] = min(dp[i], a[j]) (i = 0 or dp[i - 1] < a[i])
'''

dp = []
dp.append(a[0])

for i in range(n):
    # dpの末尾よりもa[i]が大きければ末尾に追加
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        # それ以外，a[i]より小さい最大要素の次に追加
        pos = bisect.bisect_left(dp, a[i])
        dp[pos] = a[i]

print(len(dp))