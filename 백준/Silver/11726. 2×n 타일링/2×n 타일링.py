import sys 
input = sys.stdin.readline
print = sys.stdout.write
dp = [1, 2]
n = int(input())
for i in range(2, n):
    dp.append((dp[i - 1] + dp[i - 2]) % 10007)
print("%d" % dp[n - 1])