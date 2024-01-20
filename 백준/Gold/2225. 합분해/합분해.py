import sys
from math import comb
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for __ in range(n + 1)]
for i in range(0, n + 1):
    dp[i][1] = 1

for l in range(k):
    # 사용한 수 개수
    for i in range(n + 1):
        for j in range(i + 1):
            # 이전 dp
                dp[i][l + 1] += dp[i - j][l]
                dp[i][l + 1] %= 1000000000
print("%d" % dp[n][k])
        
