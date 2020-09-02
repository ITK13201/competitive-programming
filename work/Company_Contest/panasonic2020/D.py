N = int(input())

def dfs(s, mx):
    if len(s) == N:
        print(s)
    else:
        c = 'a'
        for i in range(ord('a'), mx + 1):
            c = chr(i)
            if c == chr(mx):
                dfs(s + c, mx + 1)
            else:
                dfs(s + c, mx)

dfs('', ord('a'))