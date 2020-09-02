from collections import deque

inf = float('inf')
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = 0

# bfs
for si in range(h):
    for sj in range(w):
        if s[si][sj] == '#':
            continue
        dist = [[-inf for j in range(w)] for i in range(h)]
        q = deque()
        
        def update(i, j, x):
            if dist[i][j] != -inf:
                return
            dist[i][j] = x
            q.append([i, j])
        
        update(si, sj, 0)
        
        while len(q):
            i = q[0][0]
            j = q[0][1]
            q.popleft()
            for dir in range(4):
                ni = i + di[dir]
                nj = j + dj[dir]
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    continue
                if s[ni][nj] == '#':
                    continue
                update(ni, nj, dist[i][j] + 1)

        # 2次元配列のmax
        dist_max = max(list(map(lambda x: max(x), dist)))
        ans = max(ans, dist_max)

print(ans)