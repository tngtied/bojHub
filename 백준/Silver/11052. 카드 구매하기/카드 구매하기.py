import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0]
for i in range(1, n + 1):
    count = 0
    cand = 0
    for j in range(1, n + 1):
        if (i - j >= 0):
            cand = max(cand, cards[j] + dp[i - j])
    dp.append(cand)
print("%d" % dp[n])