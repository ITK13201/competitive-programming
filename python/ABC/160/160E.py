X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)

pqr = sorted(p[:X] + q[:Y] + r, reverse=True)
ans = sum(pqr[:X + Y])

print(ans)

