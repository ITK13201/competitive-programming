# section_scheduling.py - 区間スケジューリング問題

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

'''input
5
1 2 4 6 8
3 5 7 9 10
'''

itv = []
for i in range(n):
    itv.append([s[i], t[i]])
itv.sort(key=lambda x:x[1])

ans = 0
# 最後に選んだ仕事の終了時間
ed  = 0
for i in range(n):
    if ed < itv[i][0]:
        ans += 1
        ed = itv[i][1]

print(ans)