import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
x, y, p = map(int, input().split())
pipes = [[False for __ in range(m)] for _ in range(n)]
pipes[x][y] = True
dxy = [(1, 0), (0,1), (-1, 0),(0, -1)]
answer = 0
def dfs(before, cx, cy, curp, pipes, water):
    ## up 0 right 1 down 2 left 3
    global answer
    if (answer < water):
        answer = max(answer, water)
    for d in range(4):
        nx, ny = cx + dxy[d][0], cy + dxy[d][1]
        if (nx < 0 or ny < 0 or nx >= n or ny >= m or pipes[nx][ny] == True):
            continue
        pipes[nx][ny] = True
        if (before == d and curp >= 1):
            dfs(d, nx, ny, curp - 1, pipes, water + board[nx][ny])
        elif curp >= 2:
            dfs(d, nx, ny, curp - 2, pipes, water + board[nx][ny])
        pipes[nx][ny] = False
for i in range(4):
    dfs(i, x, y, p, pipes, board[x][y])
print("%d" % answer)