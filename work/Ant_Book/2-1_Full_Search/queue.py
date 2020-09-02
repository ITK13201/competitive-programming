from collections import deque

s = deque()

s.append(1) # 追加
s.append(2)
s.append(3)
print(s)

s.popleft() # 取り出し
print(s)
s.popleft()
print(s)
s.popleft()
print(s)