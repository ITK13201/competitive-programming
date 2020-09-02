N, A, B = map(int, input().split())

sumAB = A + B
c = N // sumAB
k = N % sumAB
if k < A:
    ans = A * c + k
else:
    ans = A * c + A

print(ans)
