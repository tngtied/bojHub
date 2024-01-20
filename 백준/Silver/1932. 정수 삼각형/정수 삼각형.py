import sys
from itertools import combinations
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
dp = []
dp.append([int(input())])
for i in range(1, n):
    nums = list(map(int, input().split()))
    dp_list = []
    for j in range(i + 1):
        if (j == 0):
            dp_list.append(dp[i - 1][0] + nums[0])
        elif(j == i):
            dp_list.append(dp[i - 1][i - 1] + nums[i])
        else:
            temp = max(dp[i - 1][j - 1], dp[i - 1][j]) + nums[j]
            dp_list.append(temp)
    dp.append(dp_list)
print("%d" % (max(dp[n - 1])))