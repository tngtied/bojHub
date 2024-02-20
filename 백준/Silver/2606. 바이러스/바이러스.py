import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
m = int(input())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
def bfs(i):
    dq = deque()
    dq.append(i)
    visit = [False] * n
    visit[i] = True
    count = 0
    while (dq):
        u = dq.popleft()
        for v in edges[u]:
            if (visit[v]):
                continue
            visit[v] = True
            count += 1
            dq.append(v)
    return count
print("%d" % bfs(0))