N, T = map(int, input().split())
T += 0.5
ab = []
for _ in range(N):
    abi = list(map(int, input().split()))
    ab.append(abi)

ab.sort(key=lambda x:x[0] // (x[1] + 1), reverse=True)
print(ab)

t = 0
t += 1
i = 0
while True:
    tt = ab[i][0] * t + ab[i][1]
    t += tt

    print('i:' + str(i) + ' t:' + str(t))
    if t > T:
        break

    i += 1
    t += 1


print(i)

