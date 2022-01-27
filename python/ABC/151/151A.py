c = str(input())

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alpha)):
    if c[0] == alpha[i]:
        ans = alpha[i + 1]

print(ans)