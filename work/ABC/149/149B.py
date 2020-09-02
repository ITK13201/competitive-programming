A, B, K = map(int, input().split())

if A >= K:
    A -= K
elif A + B >= K:
    B -= K - A
    A = 0
else:
    A = 0
    B = 0

print('{} {}' .format(A, B))