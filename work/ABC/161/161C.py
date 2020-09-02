N, K = map(int, input().split())

# x -> abs(x - K)
x = N

tmp = x // K
x -= K * tmp

if x > abs(K - x):
    x = abs(K - x)

print(x)