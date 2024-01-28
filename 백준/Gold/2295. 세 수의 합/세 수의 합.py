import sys
from bisect import bisect_right
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())

arr1 = []
arr2 = set()
for i in range(n):
    arr1.append(int(input()))

for i in range(n):
    for j in range(n):
        arr2.add(arr1[i] + arr1[j])

arr1.sort() 
def solution():
    for i in range(n):
        k = arr1[n - 1 - i]
        for x in arr1:
            z_y = k - x
            if (z_y in arr2):
                print("%d" % k)
                return
            
solution()
