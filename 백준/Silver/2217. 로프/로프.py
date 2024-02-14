import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort()
result = 0
for i in range(n):
    result = max(result, (n - i) *ropes[i])
print("%d" % result)