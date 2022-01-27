from numpy import *

N = int(input())

l = zeros((10, 10), dtype=int)

for i in range(N):
    a = int( str(i + 1)[0] )
    b = int( str(i + 1)[-1] )
    l[a][b] += 1

count = 0
for i in range(1, 10):
    for j in range(1, 10):
        count += l[i][j] * l[j][i]


print(count)
