from collections import deque

K = int(input())

lunlun = deque()

for i in range(1, 10):
    lunlun.append(i)

for i in range(K - 1):
    x = lunlun[0]
    lunlun.popleft()
    if x % 10 != 0:
        res = 10 * x + x % 10 - 1
        lunlun.append(res)
        
    res = 10 * x + x % 10
    lunlun.append(res)

    if x % 10 != 9:
        res = 10 * x + x % 10 + 1
        lunlun.append(res)
    

print(lunlun[0])