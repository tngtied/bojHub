import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
ptrA, ptrB = 0, 0
arrA.sort()
arrB.sort()
for _ in range(n + m):
    if (ptrB < m and (ptrA >= n or arrA[ptrA] > arrB[ptrB])):
        print("%d " % arrB[ptrB])
        ptrB += 1
    else:
        print ("%d " % arrA[ptrA])
        ptrA += 1