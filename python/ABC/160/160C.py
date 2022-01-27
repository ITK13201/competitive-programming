K, N = map(int, input().split())
A = list(map(int, input().split()))

l = []
# [0, 1] -> [0]
for i in range(N - 1):
    x = A[i + 1] - A[i]
    l.append(x)

x_last = (K - A[-1]) + A[0]
l.append(x_last)
#print(x_last)

max_value = max(l)
#max_index = l.index(max_value)

ans = K - max_value

print(ans)

