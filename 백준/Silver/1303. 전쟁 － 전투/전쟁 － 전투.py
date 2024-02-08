import sys
input = sys.stdin.readline
print = sys.stdout.write
from queue import deque
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sx, sy):
    visit[sy][sx] = True
    dq = deque()
    count = 0
    dq.append((sx, sy))
    while (dq):
        u = dq.popleft()
        count += 1
        for d in dxy:
            nx, ny = u[0] + d[0], u[1] + d[1]
            if (0 <= nx < n and 0 <= ny < m and inp[u[1]][u[0]] == inp[ny][nx] and not visit[ny][nx]):
                visit[ny][nx] = True
                dq.append((nx, ny))
    return count

n, m = map(int, input().split())
visit = [[False for __ in range(n)] for _ in range(m)]
inp = []
for i in range(m):
    inp.append(list(input()))
result = [0, 0]
for i in range(m):
    for j in range(n):
        if (not visit[i][j]):
            if (inp[i][j] == "W"):
                result[0] += bfs(j, i) ** 2
            else:
                result[1] += bfs(j, i) ** 2
print("%d %d" % (result[0], result[1]))