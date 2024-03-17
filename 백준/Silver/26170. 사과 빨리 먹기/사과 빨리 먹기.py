import sys
input = sys.stdin.readline
print = sys.stdout.write
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
sx, sy = map(int, input().split())
scores = [[[float("INF"), float("INF"), float("INF"),  float("INF")] for __ in range(5)] for _ in range(5)]
answer = float("INF")
def dfs(board, cx, cy, cur):
    global answer
    if cur == 3:
        answer = min(answer, scores[cx][cy][3])
        return

    for dxy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        nx = cx + dxy[0]
        ny = cy + dxy[1]
        if (nx<0 or ny<0 or nx>=5 or ny >=5):
            continue
        if board[nx][ny] == -1:
            continue
        # print("(%d, %d: %d)" % (nx, ny, cur))
        if board[nx][ny] == 1:
            board[nx][ny] = -1
            scores[nx][ny][cur + 1] = scores[cx][cy][cur] + 1
            dfs(board, nx, ny, cur + 1)
            board[nx][ny] = 1            
        elif scores[cx][cy][cur] + 1 <= scores[nx][ny][cur]:
            board[nx][ny] = -1
            scores[nx][ny][cur] = scores[cx][cy][cur] + 1
            dfs(board, nx, ny, cur)
            board[nx][ny] = 0
scores[sx][sy][0] = 0 
board[sx][sy] = -1
dfs(board, sx, sy, 0)
if (answer != float("INF")):
    print("%d" % answer)
else:
    print("-1")