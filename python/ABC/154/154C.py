N = int(input())
A = list(map(int, input().split()))

A.sort()

count = 0
for i in range(N-1):
    if A[i] == A[i+1]:
        count += 1
        break

if count == 0:
    print('YES')
else:
    print('NO')    