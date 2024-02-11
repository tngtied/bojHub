import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr.sort()
ptrA, ptrB, count = 0, n - 1, 0
while (ptrA < ptrB):
    x = arr[ptrA] + arr[ptrB]
    if (x == k):
        count += 1
        ptrA += 1
    elif (x < k):
        ptrA += 1
    else:
        ptrB -= 1
print("%d" % count)