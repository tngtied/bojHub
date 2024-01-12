import sys
from queue import PriorityQueue
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
pq = PriorityQueue()
edges = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, w = map(int, input().split())
    edges[a].append((w, b))
    edges[b].append((w, a))
s, t = map(int, input().split())
distance = [float("inf")] * (n + 1)
distance[s] = 0
pq.put((0, s))

while (not pq.empty()):
    el = pq.get()
    if (distance[el[1]] < el[0]):
        continue
    for e in edges[el[1]]:
        if (distance[e[1]] > distance[el[1]] + e[0]):
            distance[e[1]] = distance[el[1]] + e[0]
            pq.put((distance[e[1]], e[1]))
print(str(distance[t]))


    