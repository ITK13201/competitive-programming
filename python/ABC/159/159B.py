from collections import deque

def reverse(p):
    q = p[::-1]
    if p == q:
        return True
    else:
        return False


S = input()

N = len(S)

pt1 = (N - 1) // 2 - 1
pt2 = (N + 3) // 2 - 1

ptS1 = S[:pt1 + 1]
ptS2 = S[pt2:]

#print(ptS1, ptS2)

#print(reverse(ptS1), reverse(ptS2))

if reverse(S) and reverse(ptS1) and reverse(ptS2):
    print('Yes')
else:
    print('No')