import sys
input = sys.stdin.readline
print = sys.stdout.write
n, k = map(int, input().split())
count = (k * (k + 1)) // 2
if (count > n):
    print("-1")
elif ((n - count) % k == 0):
    print ("%d" % (k - 1))
else :
    print("%d" % k)
