import sys
input = sys.stdin.readline
print = sys.stdout.write

def solution():
    target, base = map(list, input().strip().split())
    count = 0
    n = len(target)
    for el in base:
        if (el == target[count]):
            count += 1
        if (count == n):
            return True
    return False


while True:
    try:
        if (solution()):
            print("Yes\n")
        else:
            print("No\n")
    except:
        break