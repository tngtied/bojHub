import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())

vertical = [False] * n
left = [False] * (2 * n - 1)
## x + y
right = [False] * (2 * n - 1)
## x - y + n - 1

def solution(pos, count):
    if (pos // n == n - 1):
        if count == n:
            return 1
        else:
            return 0
    result = 0
    for i in range(n):
        npos = (pos // n + 1) * n + i
        x = npos // n 
        y = npos % n
        l = x + y
        r = x - y + n - 1
        if (vertical[y] or left[l] or right[r]):
            continue

        vertical[y] = left[l] = right[r] = True
        result += solution(npos, count + 1)
        vertical[y] = left[l] = right[r] = False
    return result

print("%d" % solution(-1, 0))
