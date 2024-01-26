import sys
input = sys.stdin.readline
print = sys.stdout.write

def get_count(length):
    count = 0
    for lan in lans:
        count += lan // length
    return count

def lb(sr, target):
    l = 1
    r = sr
    while (l<r):
        mid = (l + r)//2
        if (get_count(mid) >= target):
            l = mid + 1
        else:
            r = mid 
    return l - 1


k, n = map(int, input().split())
lans = []
for i in range(k):
    lans.append(int(input()))
m = (sum(lans) // k) * 2
print("%d" % (lb(m, n)))
