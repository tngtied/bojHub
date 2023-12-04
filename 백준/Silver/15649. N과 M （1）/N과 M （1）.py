import sys
from copy import copy
# from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
flag = False

def max_profit(current, seq):
    global flag
    if (current == M):
        if (flag):
            print("\n")
        flag = True
        print(' '.join(map(str, seq)))
        return 0
    for i in range(1, N + 1):
        if (i in seq):
            continue
        next_seq = copy(seq)
        next_seq.append(i)
        max_profit(current + 1, next_seq)
max_profit(0, [])