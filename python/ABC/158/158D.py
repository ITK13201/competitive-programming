from collections import deque

import time

start = time.time()

S = input()
S = deque(S)
Q = int(input())
Query1 = 0
flag = False
for i in range(Q):
    Queryi = input().split()
    if Queryi[0] == '1':
        Query1 += 1
        flag = not flag
    else:
        if (Queryi[1] == '1') ^ flag:
            S.appendleft(Queryi[2])
        else:
            S.append(Queryi[2])

if Query1 % 2 != 0:
    S.reverse()

ans = ''.join(S)
print(ans)

finish = time.time()
elapsed_time_s = finish - start
elapsed_time_ms = elapsed_time_s * 1000
print('time: {}ms'.format(elapsed_time_ms))