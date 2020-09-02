S = str(input())

l = len(S)
l2 = int(l / 2)

count = 0
for i in range(l2):
    if not S[i] == S[l - i - 1]:
        count += 1

print(count)