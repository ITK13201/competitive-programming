inf = float('inf')

n = int(input())
x = []
l = []
for _ in range(n):
    xx, ll = map(int, input().split())
    x.append(xx)
    l.append(ll)

st = []
for i in range(n):
    s = x[i] - l[i]
    t = x[i] + l[i]
    st.append([s, t])

st.sort(key=lambda x:x[1])

ans =0
cur = -inf
for i in range(n):
    if cur <= st[i][0]:
        ans += 1
        cur = st[i][1]


print(ans)