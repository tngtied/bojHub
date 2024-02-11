import sys
input = sys.stdin.readline
print = sys.stdout.write
n, d, k, c = map(int, input().split())
flag = [0] * (d + 1)
arr = []
for _ in range(n):
    arr.append(int(input()))
result = 0

count = 0
for i in range(k):
    ptr = i
    flag[arr[ptr]] += 1
    if (flag[arr[ptr]] == 1):
        count += 1
if (flag[c] == 0):
    result = max(result, count + 1)
else:
    result = max(result, count)


for l in range(n):
    flag[arr[l]] -= 1
    if (flag[arr[l]] == 0):
        count -= 1
    r = l + k 
    if (r >= n):
        r -= n
    flag[arr[r]] += 1
    if (flag[arr[r]] == 1):
        count += 1
    if (flag[c] == 0):
        result = max(result, count + 1)
    else:
        result = max(result, count)
    if (result == k + 1):
        break;
print ("%d" % result)
