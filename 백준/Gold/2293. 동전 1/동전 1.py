import sys 
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
vals = [0] * (k + 1)
for i in range(n):
    coin = int(input())
    if (coin<=k):
        vals[coin] += 1
    for v in range(k + 1):
        if (v + coin > k):
            break
        vals[v + coin] += vals[v]
print("%d" % vals[k])

