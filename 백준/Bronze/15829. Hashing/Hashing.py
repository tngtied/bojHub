import sys
input = sys.stdin.readline
print = sys.stdout.write

r = 31
m = 1234567891
n = int(input())
inp = list(input().strip())
result = 0
for i in range(n):
    result = (result + ((ord(inp[i]) - ord("a") + 1) * (r ** i))) % m
print("%d" % result)