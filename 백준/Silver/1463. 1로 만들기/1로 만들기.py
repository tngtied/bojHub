import sys

input = sys.stdin.readline
print = sys.stdout.write

dp = [0, 0, 1, 1]
n = int(input())
for i in range(4, n + 1):
    cand = dp[i - 1] + 1
    if (i % 2 == 0):
        cand = min (cand, dp[int(i / 2)] + 1)
    if (i % 3 == 0):
        cand = min (cand, dp[int(i / 3)] + 1)
    dp.append(cand)
print("%d" % dp[n])