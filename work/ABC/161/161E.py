N, K, C = map(int, input().split())
S = list(input())

for i in range(N - (C + 1)):
    if S[i] == 'o':
        for j in range(i + 1, i + C + 1):
            S[j] = 'x'

for i in range(N):
    if S[i] == 'o':
        print(i + 1)