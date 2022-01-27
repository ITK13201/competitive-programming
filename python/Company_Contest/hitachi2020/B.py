A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = []
y = []
c = []
for i in range(M):
    X, Y, C= map(int, input().split())
    x.append(X-1)
    y.append(Y-1)
    c.append(C)

value = []
for i in range(M):
    v = a[x[i]] + b[y[i]] - c[i]
    value.append(v)

mindefalt = min(a) + min(b)
minvalue = min(value)

if mindefalt > minvalue:
    print(minvalue)
else:
    print(mindefalt)


