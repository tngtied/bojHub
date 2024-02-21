import sys, math
input = sys.stdin.readline
print = sys.stdout.write
r, c, w = map(int, input().split())
result = 0
for i in range(r, r + w):
    for j in range(c, c + i - r + 1):
        result += math.comb(i - 1, j - 1)
print("%d" % result)