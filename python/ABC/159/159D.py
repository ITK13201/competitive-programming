import itertools
import copy

N = int(input())
A = list(map(int, input().split()))

for k in range(N):
    ai = copy.copy(A)
    ai.pop(k)
    
    ans = 0
    for i in range(N-1):
        for j in range(i, N-1):
            if ai[i] == ai[j]:
                ans += 1
        ans -= 1
    print(ans)
