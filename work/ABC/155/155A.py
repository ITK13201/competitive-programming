A, B, C = map(int, input().split())

if A == B:
    if C == A or C == B:
        print('No')
    else:
        print('Yes')
elif B == C:
    if A == B or A == C:
        print('No')
    else:
        print('Yes')
elif C == A:
    if B == A or B == C:
        print('No')
    else:
        print('Yes')
else:
    print('No')
