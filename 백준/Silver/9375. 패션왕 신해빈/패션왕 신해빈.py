import sys, math
input = sys.stdin.readline
print = sys.stdout.write
def solution():
    gears = {}
    n = int(input())
    for i in range(n):
        wear, kind = input().strip().split()
        if kind in gears:
            gears[kind] += 1
        else:
            gears[kind] = 1
    answer = 1
    for gear in gears:
        answer *= (gears[gear] + 1)
    print ("%d\n" % (answer - 1))
tc = int(input())
for _ in range(tc):
    solution()