import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
edges = [[] for _ in range(n)]
parent = [-1] * n   
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
parent[0] = 0
dq = deque()
dq.append(0)
while (dq):
    u = dq.popleft()
    for v in edges[u]:
        if (parent[v] == -1):
            parent[v] = u
            dq.append(v)
for _ in range(1, n):
    print ("%d\n" % (parent[_] + 1))