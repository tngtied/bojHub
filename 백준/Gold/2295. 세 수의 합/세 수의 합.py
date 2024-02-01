import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
inp = []
for i in range(n):
    inp.append(int(input()))
x_y = set()
inp.sort()
for i in range(n):
    for j in range(n):
        x_y.add(inp[i] + inp[j])

def solution():
    for i in range(n):
        k = inp[n - 1 - i]
        for j in range(n - i):
            z = inp[n - 1 - i - j]
            temp = k - z
            if (temp in x_y):
                print("%d" % k)
                return

solution()