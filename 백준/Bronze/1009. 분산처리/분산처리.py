import sys
input = sys.stdin.readline
print = sys.stdout.write

tc = int(input())
for i in range(tc):
    a, b = map(int, input().split())
    a %= 10 
    if (a == 0):
        solution = 10
    elif (a in (1, 5, 6)):
        solution = a
    elif (a in (4, 9)):
        b = 2 + b % 2
        solution = (a ** b) % 10
    else:
        b = 4 + b % 4
        solution = (a ** b) % 10
    print("%d\n" % solution)

    
