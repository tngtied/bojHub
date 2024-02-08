import sys
input = sys.stdin.readline
print = sys.stdout.write
tc = int(input())
from queue import deque
def solution():
    v, e = map(int, input().split())
    edges = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    visit = [0] * v
    dq = deque()
    for i in range(v):
        if (visit[i] == 0):
            visit[i] = 1
            dq.append(i)
            while(dq):
                u = dq.popleft()
                cur_visit = visit[u]
                for v in edges[u]:
                    if (visit[v] == 0):
                        visit[v] = 3 - cur_visit
                        dq.append(v)
                    elif (visit[v] != 3 - cur_visit):
                        return False
    return True
for _ in range(tc):
    if (solution()):
        print("YES\n")
    else:
        print("NO\n")
