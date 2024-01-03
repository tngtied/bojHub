import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
table = []
sumlist = []
for i in range(n):
    table.append(list(map(int, input().split())))
    sumlist.append([0] * n)
    for j in range(0, n):
        if (i == 0):
            term1 = 0
        else:
            term1 = sumlist[i-1][j]
        if (j == 0):
            term2 = 0
        else:
            term2 =  sumlist[i][j - 1] 
        if (i!= 0 and j != 0):
            term3 = sumlist[i-1][j-1]
        else:
            term3 = 0
        sumlist[i][j] = table[i][j] + term1 + term2 - term3

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 > 1):
        boxa = sumlist[x1 - 2][y2 - 1]
    else:
        boxa = 0
    if (y1 > 1):
        boxb = sumlist[x2 - 1][y1 - 2]
    else:
        boxb = 0
    if (x1 > 1 and y1 > 1):
        boxc = sumlist[x1 - 2][y1 - 2]
    else:
        boxc = 0
    ans = sumlist[x2 - 1][y2 - 1] - boxb - boxa + boxc
    print("%d\n" % (ans))


        