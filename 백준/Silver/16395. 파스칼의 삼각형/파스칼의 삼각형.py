import sys
def fascal(row, col):
    if (col == 1 or row == col):
        return 1
    return (fascal(row - 1, col) + fascal(row - 1, col - 1))
input = sys.stdin.readline
print = sys.stdout.write
n, k = map(int, input().split())
print("%d" % (fascal(n, k)))