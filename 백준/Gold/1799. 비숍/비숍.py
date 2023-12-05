import sys
from copy import copy
input = sys.stdin.readline
print = sys.stdout.write
## 입력 기반 계산
## 게임 이론 기반 계산


N = int(input())
input_board = []
left = [0] * 2 * N

for i in range(N):
    input_board.append(list(map(int, input().split())))

## 2d를 1d로 변환해 사용할 수 있지 않을까?

def solution(dex):
    if (dex >= 2 * N - 1):
        return 0
    count = 0
    if (dex < N):
        x = 0
        y = dex
    else:
        x = dex - N + 1
        y = N - 1
    ## 해당하는 대각선의 시작 지점
    ## / 자 모양으로 돈다
    while (x < N and y >= 0):
        if (input_board[y][x] == 1 and left[x - y + N] == 0):
            left[x - y + N] = 1
            count = max(count, solution(dex + 2) + 1)
            left[x - y + N] = 0
        x += 1
        y -= 1
    if (count == 0):
        count = solution(dex + 2)
    return count
print(str(solution(0) +  solution(1)))