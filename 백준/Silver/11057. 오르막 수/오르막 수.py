import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
dp = [[1 for _ in range(10)] for __ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(10):
        count = 0
        for k in range(j + 1):
            count +=  dp[i - 1][k]
        dp[i][j] = count % 10007
# print("%s" % str(dp))
print("%d" % (sum(dp[n - 1]) % 10007))