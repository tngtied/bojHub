import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
n, m = map(int, input().split())
inp = []
for i in range(n):
    inp.append(list(map(int,input().split())))
dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visit = [[False for __ in range(m)] for _ in range(n)]

def bfs(sy, sx):
    dq = deque()
    dq.append((sy, sx))
    count = 0
    visit[sy][sx] = True
    while(dq):
        u = dq.popleft()
        count += 1
        for d in dxy:
            ny, nx = u[0] + d[0], u[1] + d[1]
            if (0 <= ny < n and 0 <= nx < m and inp[ny][nx] == 1 and not visit[ny][nx]):
                visit[ny][nx] = True
                dq.append((ny, nx))
    return count

answer = 0
max_result = 0
for i in range(n):
    for j in range(m):
        if (inp[i][j] == 1 and not visit[i][j]):
            answer += 1
            max_result = max(max_result, bfs(i, j))

print("%d\n%d" %(answer, max_result))