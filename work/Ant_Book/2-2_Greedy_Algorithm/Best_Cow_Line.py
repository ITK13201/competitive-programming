# Best_Cow_Line.py - Best Cow Line (POJ)

N = int(input())
S = list(input())

'''input
6
ABCDBCB
'''

# S[a], S[a+1], ... , S[b] が残っている配列
a = 0
b = N - 1
ans = []
while a <= b:
    # 左から見た場合と右から見た場合を比較
    left = False
    i = 0
    while a + i <= b:
        if S[a + i] < S[b - i]:
            left  = True
            break
        elif S[a + i] > S[b - i]:
            left = False
            break
        i += 1
    
    if left:
        ans.append(S[a])
        a += 1
    else:
        ans.append(S[b])
        b -= 1


print(''.join(ans))

