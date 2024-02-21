import sys, math
input = sys.stdin.readline
print = sys.stdout.write
n, k = map(int, input().split())
print ("%d" % (math.comb(n, k) % 10007))
