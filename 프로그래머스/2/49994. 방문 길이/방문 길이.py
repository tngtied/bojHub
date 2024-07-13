def solution(dirs):
    visit = [[False for __ in range(21)] for _ in range(21)]
    pos = [10, 10]
    dir_list = list(dirs)
    visit[10][10] = True
    answer = 0

    for command in dir_list:
        if command == 'U':
            if pos[1] > 0:
                pos[1] -= 1
        elif command == 'D':
            if pos[1] < 20:
                pos[1] += 1
        elif command== 'L': 
            if pos[0] > 0:
                pos[0] -= 1
        else:
            if pos[0] < 20:
                pos[0] += 1
        if not visit[pos[0]][pos[1]] and (sum(pos) % 2 == 1):
            answer += 1
            print(f"road {pos[0]} {pos[1]} not visited")
        visit[pos[0]][pos[1]] = True
        if command == 'U':
            if pos[1] > 0:
                pos[1] -= 1
        elif command == 'D':
            if pos[1] < 20:
                pos[1] += 1
        elif command== 'L': 
            if pos[0] > 0:
                pos[0] -= 1
        else:
            if pos[0] < 20:
                pos[0] += 1
        
        
    return answer