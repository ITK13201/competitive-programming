N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

first = [i+1 for i in range(N)]
end = [i+1 for i in range(N)]

def ok(arr):
    for i in range(N):
        if arr[i] != B[i]:
            return False
    
    return True


H = -1
K = -1
for p in range(M):
    for q in range(N-1):
        for i in range(M):
            if i == p:
                end[q], end[q+1] = end[q+1], end[q]

            end[A[i]-1], end[A[i]+1-1] = end[A[i]+1-1], end[A[i]-1]

        if ok(end):
            H = p
            K = q+1
            break

if H == -1 and K == -1:
    for q in range(N-1):
        end[q], end[q+1] = end[q+1], end[q]
        if ok(end):
            H = M+1
            K = q+1

if H == -1 and K == -1:
    print(-1)
    exit()

print(first)
print(end)

print(str(H), str(K))