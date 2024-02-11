import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
r = 1
result = 0
count = 0
for l in range(1, n + 1):
    while (count < n and r <= n):
        count += r
        r += 1
    if (count == n):
        result += 1
    count -= l
print("%d" % result)