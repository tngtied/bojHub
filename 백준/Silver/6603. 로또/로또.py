import sys
from itertools import combinations
input = sys.stdin.readline
print = sys.stdout.write
flag = False
while True:
    if (flag):
        print("\n")
    flag = True
    arr = list(map(int, input().split()))
    if len(arr) == 1 and arr[0] == 0:
        break
    answer = combinations(arr[1:], 6)
    for ans in answer:
        for a in ans:
            print ("%d " % a)
        print ("\n")
    