import sys
from copy import copy
input = sys.stdin.readline
print = sys.stdout.write
## 입력 기반 계산
## 게임 이론 기반 계산


N = int(input())
input_board = list(map(int, input().split()))

def not_win(x, y, board):
    if (board[x] != 0):
        return False
    for i in range(N):
        ## board 내부 x 좌표
        if (i == x or (board[i] == 0)):
            continue
        if (board[i] == y):
            return False
        if (abs(i - x) == abs(board[i] - y)):
            return False
    return True 

def solution(board, x):
    if (x == N):
        for i in range(N):
            if (board[i] == 0):
                return False
        print(' '.join(map(str, board)))
        return True
    if (board[x] != 0):
        if (solution(board, x + 1)):
            return True
    else:
        for i in range(1, N + 1):
            if (not_win(x, i, board)):
                new_board = copy(board)
                new_board[x] = i
                if (solution(new_board, x + 1)):
                    return True
    return False
if (not solution(input_board, 0)):
    print("-1")