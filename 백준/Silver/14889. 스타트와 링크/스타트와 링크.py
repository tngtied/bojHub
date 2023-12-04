import sys
from copy import copy
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
input_board = []
for i in range(N):
    input_board.append(list(map(int, input().split())))

min_diff = float('inf')

def cal_skill(flag, team):
    ##if flag: team
    ##if not flag: not team
    result = 0
    for a in range(N):
        if ((flag and a not in team) or (not flag and a in team)):
            continue
        for b in range(N):
            if ((flag and b not in team) or (not flag and b in team)):
                continue
            result += input_board[a][b]
    return result

def solution(pick, sp, team):
    global input_board, min_diff
    if (pick == N / 2):
        min_diff = min(min_diff, abs(cal_skill(True, team) - cal_skill(False, team)))
        return
    for i in range(sp, N):
        new_team = copy(team)
        new_team.append(i)
        solution(pick + 1, i + 1, new_team)
solution(0, 0, [])
print(str(min_diff))