import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
arr = list(map(int, input().split()))
count = 0
result = 0
highest = 0
for i in range(n):
    if (arr[i] > highest):
        result = max(result, count)
        count = 0
        highest = arr[i]
    elif (arr[i] < highest):
        count += 1
result = max(count, result)
print("%d" % result)