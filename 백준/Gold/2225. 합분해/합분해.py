import sys 
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())

dp = [[0 for __ in range(k)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] += 1
    
for i in range(n + 1):
    for j in range(1, k):
        for l in range(i + 1):
            dp[i][j] += dp[i - l][j - 1]
            dp[i][j] %= 1000000000

print("%d" % dp[n][k - 1])