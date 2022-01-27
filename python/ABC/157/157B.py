import numpy as np
import sys

A = []
for i in range(3):
    array = list(map(int, input().split()))
    A.append(array)
N = int(input())
b = []
for i in range(N):
    k = int(input())
    b.append(k)

for k in range(len(b)):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if b[k] == A[i][j]:
                A[i][j] = 0


s_row = np.sum(A, axis=1)
for i in range(3):
    if s_row[i] == 0:
        print('Yes')
        sys.exit()


s_col = np.sum(A, axis=0)
for i in range(3):
    if s_col[i] == 0:
        print('Yes')
        sys.exit()

c = 0
for i in range(3):
    c += A[i][i]
if c == 0:
    print('Yes')
    sys.exit()

c = 0
for i in range(3):
    c += A[3-i-1][i]
if c == 0:
    print('Yes')
    sys.exit()

print('No')