X, Y, Z = map(int, input().split())

tmp = X
X = Y
Y = tmp

tmp = X
X = Z
Z = tmp

print(X, Y, Z)