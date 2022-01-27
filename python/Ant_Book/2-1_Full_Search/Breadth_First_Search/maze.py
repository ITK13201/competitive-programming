# maze.py - 迷路の最短路

INF = 10**9

from collections import deque

# N*M matrix
N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

'''input
10 10
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#
'''

def start_goal():
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 'S':
                sx = i
                sy = j
            if maze[i][j] == 'G':
                gx = i
                gy = j
    return sx, sy, gx, gy

sx, sy, gx, gy = start_goal()
# 移動4方向のベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# (sx, sy) から (gx, gy) への最短距離を求める
# 辿り着けないとINF
def bfs():
    que = deque()
    # 全ての点をINFで初期化
    d = [[INF for j in range(M)] for i in range(N)]
    # スタート地点をキューに入れ，その点の距離を0にする
    que.append([sx, sy])
    d[sx][sy] = 0
    
    # キューが空になるまでループ
    while len(que):
        # キューの先頭を取り出す
        p = que[0]
        que.popleft()
        # 取り出してきた状態がゴールなら探索をやめる
        if p[0] == gx and p[1] == gy:
            break
        # 移動4方向をループ
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
        
            # 1. 移動が可能かの判定
            # 2. すでに訪れたことがあるかの判定(d[nx][ny] != INF なら訪れたことがある)
            if 0 <= nx and nx < N and 0 <= ny and ny < M and maze[nx][ny] != '#' and d[nx][ny] == INF:
                # 移動できるならキューに入れ，その点をpからの距離+1で確定する
                que.append([nx, ny])
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gx][gy]


res = bfs()
print(res)