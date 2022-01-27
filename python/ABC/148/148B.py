N = int(input())
S, T = map(str, input().split())

STlen = len(S)

ans = ''

for i in range(STlen):
    ans += S[i]
    ans += T[i]

print(ans)