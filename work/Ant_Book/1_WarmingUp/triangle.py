n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            length = a[i] + a[j] + a[k] # 周長
            bar_max = max(a[i], a[j], a[k]) # 最長の棒の長さ
            rest = length - bar_max # 他の二本の合計
            
            if bar_max < rest:
                ans = max(ans, length)

print(ans)
