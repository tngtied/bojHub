def solution(maps):
    from collections import deque
    dq = deque()
    dq.append([0, 0, 1])
    dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visit = [[False for __ in range(len(maps[0]))] for _ in range(len(maps))]
    visit[0][0] = True
    while dq:
        cx, cy, cost = dq.popleft()
        if cx == len(maps) - 1 and cy == len(maps[0]) - 1:
            return cost
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visit[nx][ny] and maps[nx][ny]:
                visit[nx][ny] = True
                dq.append([nx, ny, cost + 1])
                
    return -1