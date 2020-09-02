from numpy import *

N, M = map(int, input().split())
p = zeros(M, dtype=int)
S = []
for i in range(M):
    x, y = input().split()
    p[i] = int(x) - 1
    S.append(y)

ac = zeros(N, dtype=int)
wa = zeros(N, dtype=int)
s_ac = 0
s_wa = 0
for i in range(M):
    if ac[p[i]] == 0:
        if S[i] == 'AC':
            ac[p[i]] += 1
            s_ac += 1
            s_wa += wa[p[i]]
        elif S[i] == 'WA':
            wa[p[i]] += 1
    else:
        pass

print('{} {}'.format(s_ac, s_wa))

