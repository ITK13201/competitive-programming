n = int(input())
m = int(input())
k = list(map(int, input().split()))

f = False

for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if k[a] + k[b] + k[c] + k[d] == m:
                    f = True
                    break

if f:
    print('Yes')
else:
    print('No')