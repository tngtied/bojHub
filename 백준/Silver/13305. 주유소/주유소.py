import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

liters = float("INF")
result = 0
for i in range(n - 1):
    liters = min(liters, city[i])
    result += liters * road[i]
print("%d" % result)