N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
    if A[i] % 2 == 0:
        B.append(A[i])

count = 0
for i in range(len(B)):
    if B[i] % 3 == 0 or B[i] % 5 == 0:
        count += 1

if count == len(B):
    print('APPROVED')
else:
    print('DENIED')