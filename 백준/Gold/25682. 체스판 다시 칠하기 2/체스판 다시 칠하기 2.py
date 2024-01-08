import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M, K = map(int, input().split())

box = [[0] * (M + 1)]


def isblack(x, y):
    ## 왼쪽 위 타일이 black이라는 가정 하에
    ## 0부터 시작하는 index 기반
    if (y%2 == 0):
        yEvenFlag = True
    else:
        yEvenFlag = False
    if (x%2 == 0):
        return (yEvenFlag)
    else:
        flag = True
        if (yEvenFlag):
            flag = False
        return flag

for i in range(N):
    box.append([0] + [*input()])
sumlist = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
## upper left is black
for i in range(1, N + 1):
    for j in range(1, M + 1):
            ## 0: 왼쪽 위 타일이 black
            blackFlag = isblack(j, i)
            if ((blackFlag and box[i][j] == "B") or (not blackFlag and box[i][j] == "W")):
                tile = 0
            else:
                tile = 1
            sumlist[i][j] += sumlist[i-1][j] +  sumlist[i][j - 1] - sumlist[i-1][j-1] + tile

def solution():
    result = K**2
    for i in range(K, N + 1):
        for j in range(K, M + 1):
            cand = sumlist[i][j] - sumlist[i - K][j] - sumlist[i][j - K] + sumlist[i - K][j - K]
            result = min(result, cand, K**2 - cand)
    return str(result)

print(str(solution()))