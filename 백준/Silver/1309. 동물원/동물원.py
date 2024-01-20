import sys
input = sys.stdin.readline
print = sys.stdout.write

n= int(input())
dp = []
## 00, 10, 01
dp.append([1, 1, 1])

for i in range(1, n):
    a = sum(dp[i - 1]) % 9901
    b = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    c = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp.append([a, b, c])
print("%d" % (sum(dp[n - 1]) % 9901))
        
