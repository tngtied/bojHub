import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
while True:
    n, m = map(int, input().split())
    if (n == 0 and m == 0):
        break
    visit = [[False for __ in range(n)] for _ in range(m)]
    maps = []
    for _ in range(m):
        maps.append(list(map(int, input().split())))
    dq = deque()
    count = 0
    for i in range(m):
        for j in range(n):
            if (maps[i][j] == 0 or visit[i][j]):
                continue
            dq.append((j, i))
            count += 1
            while dq:
                u = dq.popleft()
                for dx in (1, 0, -1):
                    for dy in (1, 0, -1):
                        nx, ny = u[0] + dx, u[1] + dy
                        # print ("(nx %d ny %d)" % (nx, ny))
                        if (nx < 0 or ny < 0 or nx >= n or ny >= m or visit[ny][nx] or maps[ny][nx] == 0):
                            continue
                    
                        visit[ny][nx] = True
                        dq.append((nx, ny))
    print("%d\n" % count)