import sys

input = sys.stdin.readline
print = sys.stdout.write


def solve():
    n, m, w = map(int, input().strip().split())
    dist = [10001] * (n + 1)
    dist[1] = 0
    edges = []
    for i in range(m):
        s, e, t = map(int, input().strip().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for i in range(w):
        s, e, t = map(int, input().strip().split())
        edges.append((s, e, -t))

    dist[1] = 0
    for i in range(n):
        for j in range(m * 2 + w):
            s = edges[j][0]
            e = edges[j][1]
            t = edges[j][2]
            if (dist[e] > dist[s] + t):
                dist[e] = dist[s] + t
                if (i == n - 1):
                    return True

    return False


tc = int(input().strip())
for i in range(tc):
    if (solve()):
        print("YES\n")
    else:
        print("NO\n")