import sys

input = sys.stdin.readline
print = sys.stdout.write

dp = [(0, 0)]
##이전 계단을 밟음, 밟지 않음
n = int(input())
step = int(input())
dp.append((step, step))
for i in range(2, n + 1):
    step = int(input())
    first = dp[i - 1][1] + step
    second = max(dp[i - 2][0] + step, dp[i - 2][1] + step)
    dp.append((first, second))
print(str(max(dp[n])))