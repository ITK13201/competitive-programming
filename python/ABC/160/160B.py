X = int(input())

'''
500: 1000
5: 5
'''

ans = 0
if X >= 500:
    x500 = X // 500
    ans += x500 * 1000
    X -= 500 * x500
    #print('x500: {}'.format(x500))

if X >= 5:
    x5 = X // 5
    ans += x5 * 5
    X -= 5 * x5
    #print('x5: {}'.format(x5))

print(ans)