import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
arr = list(map(int, input().split()))
count = 0
# 딸기, 초코, 바나나
for i in range(n):
    if (arr[i] == count % 3):
        count += 1
print("%d" % count)