import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
edges = [[] for i in range(n)]

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    edges[a - 1].append((w, b - 1))
    edges[b - 1].append((w, a - 1))
def dfs(u):
    for v in edges[u]:
        if (dist[v[1]] == -1 or dist[v[1]] > dist[u] + v[0]):
            dist[v[1]] = dist[u] + v[0]
            dfs(v[1])
    
for _ in range(n):
    edges[_].sort()
for _ in range(m):
    a, b = map(int, input().split())
    dist = [-1 for _ in range(n)]
    dist[a - 1] = 0
    dfs (a - 1)
    print ("%d\n" % dist[b - 1])
