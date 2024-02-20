import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10000)
n = int(input())
nodes = list(map(int, input().split()))
edges = [[] for _ in range(n)]

for i in range(n):
    if (nodes[i] == -1):
        sp = i
    else:
        edges[nodes[i]].append(i)
deleted = int(input())
result = 0
def dfs(u):
    global result
    count = 0
    for v in edges[u]:
        if (v == deleted):
            continue
        dfs(v)
        count += 1
    if count == 0:
        result += 1
if (sp != deleted):
    dfs(sp)

print ("%d" % result)