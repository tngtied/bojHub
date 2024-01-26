import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
target = []
for i in range(n):
    target.append(int(input()))

from collections import deque
stack = deque()
sp = 1
result = []
flag = True
for t in target:
    if (t >= sp):
        while (sp != t):
            stack.append(sp)
            result.append("+")
            sp += 1
        stack.append(sp)
        result.append("+")
        stack.pop()
        result.append("-")
        sp += 1
    else:
        if (len(stack) > 0):
            el = stack.pop()
            result.append("-")
        while (el != t and len(stack) > 0):
            el = stack.pop()
            result.append("-")
        
        if (el != t):
            print("NO")
            flag = False
            break
if (flag):
    for r in result:
        print("%c\n" % r)
            
