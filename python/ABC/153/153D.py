def f(x):
    if x == 1:
        return 1
    else:
        return 2 * f(x // 2) + 1   

H = int(input())

min = f(H)

print(min)