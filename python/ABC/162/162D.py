N = int(input())
S = list(input())

def BinarySeach(data, key):
    l = 0
    r = len(data)

    while r - l >= 1:
        m = (l + r) // 2
        guess = data[m]
        if guess == key:
            return m
        elif guess < key:
            l = m + 1
        else:
            r = m
            
    return 100

def ok(st, i, j):
    k = BinarySeach(S, st)
    if k - j == j - i:
        return False
    else:
        return True

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if S[i] == 'R':
            if S[j] == 'G':
                if ok('B', i, j):
                    ans += 1
            elif S[j] == 'B':
                if ok('G', i, j):
                    ans += 1
        elif S[i] == 'G':
            if S[j] == 'B':
                if ok('R', i, j):
                    ans += 1
            elif S[j] == 'R':
                if ok('B', i, j):
                    ans += 1
        elif S[i] == 'B':
            if S[j] == 'R':
                if ok('G', i, j):
                    ans += 1
            elif S[j] == 'G':
                if ok('R', i, j):
                    ans += 1

print(ans)