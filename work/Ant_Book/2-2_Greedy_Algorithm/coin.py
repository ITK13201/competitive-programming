# coin.py - コインの問題

C = list(map(int, input().split()))
A = int(input())

'''input
3 2 1 3 0 2
620
'''

V = [1, 5, 10, 50, 100, 500]

ans = 0
for i in range(len(V)):
    ii = - i - 1
    t = min(A // V[ii], C[ii])
    A -= t * V[ii]
    ans += t

print(ans)