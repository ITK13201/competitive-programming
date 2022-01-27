def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x, 1):
        if x % i == 0:
            return False
    return True

X = int(input())
ans = X

while not is_prime(ans):
    ans += 1

print(ans)