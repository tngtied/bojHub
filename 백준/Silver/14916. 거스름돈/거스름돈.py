import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
coins = [5, 2]
count = 0
if n % 2 == 0:
    temp = n // 5
    if (temp %2 == 1):
        temp -= 1
    n -= temp * 5
    count += temp
    count += n // 2
else:
    temp = n // 5
    if temp % 2 == 0:
        temp -= 1
    if (temp <= 0):
        count = -1
    else:
        count += temp
        n -= temp * 5
        count += n //2
print("%d" % count)