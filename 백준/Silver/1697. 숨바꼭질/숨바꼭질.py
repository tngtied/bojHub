import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

s, t = map(int, input().split())
n = 200000
cur = s
dq = deque()
dq.append(s)
dp = [0] * n
visit = [False] * n
while (cur != t):
    cur = dq.popleft()
    for e in [cur - 1, cur + 1, cur * 2]:
        if (e < 0 or e > n - 1 or visit[e]):
            continue;
        dq.append(e)
        dp[e] = dp[cur] + 1
        visit[e] = True

print("%d" % dp[t])