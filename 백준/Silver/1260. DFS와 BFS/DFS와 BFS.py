import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def dfs():
    stack = deque()
    visit = [False] * n
    result = []
    stack.appendleft(v)
    while len(stack):
        e = stack.popleft()
        if (visit[e]):
            continue
        visit[e] = True
        result.append(e)
        edges[e].sort(reverse= True)
        for f in edges[e]:
            if (not visit[f]):
                stack.appendleft(f)
    return result

def bfs():
    dq = deque()
    visit = [False] * n
    result = []
    dq.append(v)
    while len(dq):
        e = dq.popleft()
        if (visit[e]):
            continue
        result.append(e)
        visit[e] = True
        edges[e].sort()
        for f in edges[e]:
            if (not visit[f]):
                dq.append(f)
    return result    


n, m, v = map(int, input().split())
v -= 1
edges = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
dfs_result = dfs()
bfs_result = bfs()
for e in dfs_result:
    print("%d " % (e + 1))
print("\n")
for e in bfs_result:
    print("%d " % (e + 1))