import sys
input = sys.stdin.readline
print = sys.stdout.write
table = list(input().strip())
length = 0
result = []
flag = False
flag2 = False
for t in table:
    if t == "X":
        length += 1
        flag2 = True
    else:
        if (length % 2 == 1):
            flag = True
            break
        As = length // 4
        Bs = (length - (As * 4)) // 2
        for _ in range(As):
            result.append("AAAA")
        for _ in range(Bs):
            result.append("BB")
        if (t == "."):
            result.append(".")
        flag2 = False
        length = 0
if flag2:
    if (length % 2 == 1):
        flag = True
    As = length // 4
    Bs = (length - (As * 4)) // 2
    for _ in range(As):
        result.append("AAAA")
    for _ in range(Bs):
        result.append("BB")
if flag:
    print ("-1")
else:
    for r in result:
        print ("%s" % r)