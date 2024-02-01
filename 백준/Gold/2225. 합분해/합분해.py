import sys
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().strip().split())
sumlist = [[0 for __ in range(k)] for _ in range(n + 1)]
for i in range(n + 1):
    sumlist[i][0] = 1
for i in range(n + 1):
    for l in range(1, k):
        for j in range(i + 1):
            sumlist[i][l] += sumlist[i - j][l - 1]
            sumlist[i][l] %= 1000000000
print("%d" % sumlist[n][k - 1])