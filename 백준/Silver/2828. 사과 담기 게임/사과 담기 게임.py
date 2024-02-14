import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
j = int(input())
pos = 1
count = 0
for i in range(j):
    npos = int(input())
    if (npos < pos):
        count += pos - npos
        pos = npos 
    if (npos < pos + m):
        continue
    else:        
        count += npos - m + 1 - pos
        pos = npos - m + 1
print("%d" % count)