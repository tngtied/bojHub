import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
n, m, k, x = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
dist = [-1] * n
dist[x - 1] = 0
dq = deque()
dq.append(x - 1)
answer = []
while dq:
    u = dq.popleft()
    if (dist[u] == k):
        answer.append(u + 1)
    for v in edges[u]:
        if (dist[v] == -1):
            dist[v] = dist[u] + 1
            dq.append(v)
answer.sort()
if (len(answer)):
    for a in answer:
        print("%d\n" % a)
else:
    print("-1")