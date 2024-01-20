import sys
from itertools import combinations
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
dp = []
dp.append(list(map(int, input().split())))
for i in range(1, n):
    costs = list(map(int, input().split()))
    R = min(dp[i - 1][1], dp[i - 1][2]) + costs[0]
    G = min(dp[i - 1][0], dp[i - 1][2]) + costs[1]
    B = min(dp[i - 1][0], dp[i - 1][1]) + costs[2]
    dp.append([R, G, B])
print("%d" % (min(dp[n - 1])))