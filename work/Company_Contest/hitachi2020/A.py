S = input()
hi = 'hi'
if len(S) % 2 == 0:
    T = len(S) // 2 * hi
    if S == T:
        print('Yes')
    else:
        print('No')
else:
    print('No')