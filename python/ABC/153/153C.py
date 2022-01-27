N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort()

if N <= K:
    min = 0
else:
    min = 0
    left = N - K
    for i in range(left):
        min += H[i]

print(min)
