import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
from collections import deque
dq = deque()
for i in range(1, n + 1):
    dq.append(i)
while (len(dq) != 1):
    dq.popleft()
    el = dq.popleft()
    dq.append(el)
print("%d" % (dq.pop()))