import sys
input = sys.stdin.readline
print = sys.stdout.write
def solution(n, costs, target):
    # costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    def findRoot(node):
        if node != parent[node]:
            parent[node] = findRoot(parent[node])
        return parent[node]
    def unionSet(u, v):
        u_r = findRoot(u)
        v_r = findRoot(v)
        parent[u_r] = v_r
    def sameRoot(u, v):
        u_r = findRoot(u)
        v_r = findRoot(v)
        return u_r == v_r
    for s, t, w in costs:
        if not sameRoot(s, t):
            unionSet(s, t)
    answer = set([findRoot(parent[i-1]) for i in target])
    return len(answer) == 1
n = int(input())
m = int(input())
edges = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if (temp[j] == 1):
            edges.append((i, j, 1))
target = list(map(int, input().split()))
if (solution(n, edges, target)):
    print("YES")
else:
    print("NO")