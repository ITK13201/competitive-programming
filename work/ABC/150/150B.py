N = int(input())
S = str(input())

a = 'ABC'
count = 0

for i in range(N):
    if S[i:i+3] == a:
        count += 1

print(count)