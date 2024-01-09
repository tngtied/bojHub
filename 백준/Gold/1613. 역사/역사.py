import sys

input = sys.stdin.readline
print = sys.stdout.write
n, k = map(int, input().split())
reachable = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(k):
    a, b = map(int, input().split())
    reachable[a][b] = -1
    reachable[b][a] = 1
for via in range(1, n + 1):
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if (reachable[u][via] != 0 and reachable[u][via] == reachable[via][v]):
                reachable[u][v] = reachable[u][via]

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    print("%d\n" % (reachable[a][b]))