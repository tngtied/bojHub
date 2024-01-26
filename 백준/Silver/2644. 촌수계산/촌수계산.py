import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
s, t = map(int, input().split())
m = int(input())
edges = [[] for _ in range(n + 1)]
rel = [-1 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

from collections import deque
def bfs():
    dq = deque()
    rel[s] = 0
    dq.append((s, 0))
    while (len(dq)):
        u = dq.pop()
        for v in edges[u[0]]:
            if (rel[v] == -1):
                rel[v] = u[1] + 1
                dq.appendleft((v, u[1] + 1))
bfs()
print("%d" % rel[t])
