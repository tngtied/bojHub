import sys
input = sys.stdin.readline
print = sys.stdout.write
k, n = map(int, input().split())
arr = list(map(int, input().split()))

r = 0
result = 0
count = 0
for l in range(k):
    while (count < n and r < k):
        count += arr[r]
        r += 1
    if (count == n):
        result += 1
    count -= arr[l]
print("%d" % result)