import sys
input = sys.stdin.readline
print = sys.stdout.write
n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
count = 1
pos = arr[0]
for i in range(1, n):
    if (arr[i] <= pos + l - 1):
        continue
    else:
        pos = arr[i]
        count += 1
print ("%d" % count)