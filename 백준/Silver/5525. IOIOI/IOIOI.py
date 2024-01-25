import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
n = int(input())
plen = n * 2 + 1
m = int(input())
string = list(input())
candA = 0
result = 0
for char in string:
    
    if (char == "I"):
        if (candA % 2 == 0):
            candA += 1
            if (candA == plen):
                result += 1
                candA -= 2
        else:
            candA = 1
    else:
        if (candA % 2 == 1):
            candA += 1
        else:
            candA = 0
            

print("%d" % (result))