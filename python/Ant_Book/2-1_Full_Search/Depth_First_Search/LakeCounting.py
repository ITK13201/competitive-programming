# LakeCounting.py - POJ Lake Counting

N, M = map(int, input().split())
field = [list(input()) for _ in range(N)]

'''input
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
'''


# 現在位置(x, y)
def dfs(x, y):
    # 今いるところを.に置き換える
    field[x][y] = '.'

    # 移動する8方向をループ
    for dx in range(-1, 1 + 1):
        for dy in range(-1, 1 + 1):
            # x方向にdx, y方向にdy, 移動した場所を(nx, ny)とする．
            nx = x + dx
            ny = y + dy

            # 1. nx, nyが庭の範囲内かどうか
            # 2. field[nx][ny]が水たまりかどうか　を判定
            if 0 <= nx and nx < N and 0 <= ny and ny < M and field[nx][ny] == 'W':
                dfs(nx, ny)
    return


res = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 'W':
            dfs(i, j)
            res += 1

print(res)
