import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n = int(input())
visit = [[False for _ in range(n)] for __ in range(n)]

def bfs(s):
    result = 0
    dq = deque()
    dq.append(s)
    while (len(dq)):
        e = dq.popleft()
        if (visit[e[0]][e[1]]):
            continue 
        result += 1
        visit[e[0]][e[1]] = True
        for d in dir:
            dx = d[0] + e[0]
            dy = d[1] + e[1]
            if (dx >= 0 and  dx <= n - 1 and dy >= 0 and dy <= n - 1 and maps[dx][dy] == 1 and not visit[dx][dy]):
                dq.append((dx, dy))
    return result

maps = []
houses = deque()
for i in range(n):
    maps.append(list(map(int, list(input().strip()))))
    for j in range(n):
        if (maps[i][j] == 1):
            houses.append((i, j))

count = 0
cases = []
while (len(houses)):
    e = houses.pop()
    if (visit[e[0]][e[1]] == False):
        cases.append(bfs(e))
        count += 1
print("%d" % count)
cases.sort()
for c in cases:
    print("\n%d" % c)

