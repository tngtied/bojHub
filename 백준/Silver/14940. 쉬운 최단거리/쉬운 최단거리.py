import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
inpmap = []
resultmap = [[-1 for __ in range(m)] for _ in range(n)]
sp = (0, 0)
for i in range(n):
    inpmap.append(list(map(int, input().split())))
    for j in range(m):
        if (inpmap[i][j] == 2):
            sp = (i, j)
        elif (inpmap[i][j] == 0):
            resultmap[i][j] = 0

dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs():
    resultmap[sp[0]][sp[1]] = 0
    dq = deque()
    dq.append(sp)
    while (len(dq)):
        p = dq.pop()
        for xy in dxy:
            nx = p[0] + xy[0]
            ny = p[1] + xy[1]
            if (0 <= nx < n and 0 <= ny < m and inpmap[nx][ny] != -1 and resultmap[nx][ny] == -1):
                if (inpmap[nx][ny] == 0):
                    resultmap[nx][ny] = 0
                else:
                    resultmap[nx][ny] = resultmap[p[0]][p[1]] + 1
                    dq.appendleft((nx, ny))
bfs()
for i in range(n):
    for j in range(m):
        print("%d " % resultmap[i][j])
    print("\n")
