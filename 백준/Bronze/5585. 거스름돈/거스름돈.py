import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
m = 1000 - n
count = 0
coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    count += m // coin
    m -= coin * (m // coin)
print("%d" % count)