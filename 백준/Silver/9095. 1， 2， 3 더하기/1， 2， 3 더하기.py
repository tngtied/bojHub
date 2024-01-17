import sys

input = sys.stdin.readline
print = sys.stdout.write

dp = [0, 1, 2, 4]
##이전 계단을 밟음, 밟지 않음
n = int(input())
tc = []
for i in range(n):
    tc.append(int(input()))

maxtc = max(tc)
for i in range (4, maxtc + 1):
    count = 0
    count += dp[i - 1]
    count += dp[i - 2]
    if (i > 3):
        count += dp[i - 3]
    dp.append(count)
for e in tc:
    print ("%d\n" % dp[e])