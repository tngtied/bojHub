import sys
input = sys.stdin.readline
print = sys.stdout.write

def n_queen(count, pos):
    if (pos // n == n - 1):
        if (count == n):
            return 1
        else:
            return 0
        
    result = 0
    for i in range(n):
        npos = (pos // n + 1) * n + i
        nx, ny = npos // n, npos % n
        left = nx + ny
        right = nx - ny + n - 1
        if (y[ny] or l[left] or r[right]):
            continue
        x[nx] = y[ny] = l[left] = r[right] = True
        result += n_queen(count + 1, npos)
        x[nx] = y[ny] = l[left] = r[right] = False
    return result
            

n = int(input())
x = [False] * (n)
y = [False] * n
l = [False] * 2 * n
r = [False] * 2 * n
print("%d" % (n_queen(0, -1)))
