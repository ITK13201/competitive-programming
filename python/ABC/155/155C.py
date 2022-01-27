from collections import Counter

N = int(input())
S = []
for i in range(N):
    m = input()
    S.append(m)

c = Counter(S)

m = max(c.values())
ans = []

for i, j in c.items():
    if j == m:
        ans.append(i)
ans.sort()

for i in ans:
    print(i)