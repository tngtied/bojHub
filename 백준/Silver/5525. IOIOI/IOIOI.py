import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
n = int(input())
plen = n * 2 + 1
m = int(input())
string = list(input())
dq = deque()
result = 0
for char in string:
    dqlen = len(dq)
    for _ in range(dqlen):
        e = dq.popleft()
        if (e % 2 == 0 and char == "I"):
            e += 1
            if (e == plen):
                result += 1
            else:
                dq.append(e)
        elif (e % 2 == 1 and char == "O"):
            e += 1
            dq.append(e)
    if (char == "I"):
        dq.append(1)
print("%d" % (result))