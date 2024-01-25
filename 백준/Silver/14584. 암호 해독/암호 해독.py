import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def check(stra, strb, diff):
    newdiff = ord(stra) - ord(strb)
    if (newdiff < 0):
        newdiff += 26
    return (diff == newdiff)

inp = input().strip()
n = int(input())
patterns = []
counts = [deque() for _ in range(n)]
## index, diff,  
for _ in range(n):
    patterns.append(list(input().strip()))
 
m = len(inp)

def check_patterns():
    for i in range(m):
        for j in range(n):
            dq = counts[j]
            dqlen = len(dq)
            for _ in range(dqlen):
                cand = dq.popleft()
                if (check(patterns[j][cand[0]], inp[i], cand[1])):
                    cand[0] += 1
                    if (cand[0] == len(patterns[j])):
                        return cand[1]
                    dq.append([cand[0], cand[1]])
            diff = ord(patterns[j][0]) - ord(inp[i])
            if (diff < 0):
                diff += 26
            dq.append([1,diff])

caesar = check_patterns()
for char in inp:
    newchar = ord(char) + caesar
    if (newchar > ord("z")):
        newchar -= 26
    print(chr(newchar))