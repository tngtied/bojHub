import sys
input = sys.stdin.readline
print = sys.stdout.write

v, e = map(int, input().split())
edges = []
for _ in range(e):
    s, t, w = map(int, input().split())
    edges.append((s - 1, t - 1, w))
edges.sort(key = lambda x : x[2])
def solution(edges, n):
    roots = [i for i in range(n)]
    result = 0
    def find_root(u):
        if (u != roots[u]):
            roots[u] = find_root(roots[u])
        return roots[u]
    def union(u, v):
        u_r = find_root(u)
        v_r = find_root(v)
        roots[u_r] = v_r
    for s, t, w in edges:
        if find_root(s) != find_root(t):
            union(s, t)
            result += w
    return result
print("%d" % solution(edges, v))