import math

A, B = map(int, input().split())

INF = 10**4
for x in range(INF):
    if math.floor(x * 0.08) == A:
        if math.floor(x * 0.10) == B:
            print(x)
            exit()

print(-1)


