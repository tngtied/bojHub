import sys
input = sys.stdin.readline
print = sys.stdout.write
l, c = map(int, input().split())
arr = list(input().strip().split())
arr.sort()
temp = ["-1" for _ in range(l)]
answer = []
def solution(vo, con, count, sdex):
    if (count == l ):
        if (vo > 0 and con > 1 ):
            answer.append("".join(temp))
        return
    for i in range(sdex, c):
        temp[count] = arr[i]
        if (arr[i] in ('a', 'e', 'i', 'o', 'u')):
            solution(vo + 1, con, count + 1, i + 1)
        else:
            solution(vo, con + 1, count + 1, i + 1)
solution(0,0,0,0)
for a in answer:
    print("%s\n" % a)