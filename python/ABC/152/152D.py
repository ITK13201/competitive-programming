from numpy import *

N = int(input())

A = zeros(N, dtype=int)
B = zeros(N, dtype=int)

al = []
bl = []

count = 0
for i in range(N):
    A[i] = i + 1
    al.append( str(A[i]) )

    a_s = (al[i])[0]
    a_e = (al[i])[-1]

    for j in range(N):
        B[j] = j + 1
        bl.append( str(B[j]) )

        b_s = (bl[j])[0]
        b_e = (bl[j])[-1]

        if a_e == b_s and a_s == b_e:
            count += 1

print(count)
