import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

x = sorted(P)
xl = list(itertools.permutations(x))

tp = tuple(P)
tq = tuple(Q)

a = xl.index(tp)
b = xl.index(tq)

ans = abs(a - b)

print(ans)