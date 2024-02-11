import sys
input = sys.stdin.readline
print = sys.stdout.write
n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = n
flag = False
count = 0
rptr = 0
for lptr in range(n):
    while (count < k and rptr < n):
        if (arr[rptr] == 1):
            count += 1
        rptr += 1
    if (count == k):
        flag = True
        result = min(result, rptr - lptr)
    if (arr[lptr] == 1):
        count -= 1
if flag:
    print("%d" % result)
else:
    print("-1")