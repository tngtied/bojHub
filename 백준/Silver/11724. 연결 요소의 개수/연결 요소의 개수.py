import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
visit = [False] * n 
for _ in range(m):
    a, b = map(int, input().split())
    edges[a-1].append(b -1)
    edges[b-1].append(a - 1)
count = 0
def bfs(s):
    dq = deque()
    dq.append(s)
    visit[s] = True
    while dq:
        u = dq.popleft()
        for v in edges[u]:
            if (visit[v]):
                continue
            visit[v] = True
            dq.append(v)
for i in range(n):
    if (visit[i]):
        continue
    else:
        count += 1
        bfs(i)
print ("%d" % (count))