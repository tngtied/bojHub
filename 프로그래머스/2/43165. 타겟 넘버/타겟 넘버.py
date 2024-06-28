def solution(numbers, target):
    from collections import deque
    dq = deque()
    dq.append([numbers[0], 0])
    dq.append([-numbers[0], 0])
    answer = 0
    while dq:
        el1, pos = dq.popleft()
        if pos == len(numbers) - 1:
            if el1 == target:
                answer += 1
        else:
            dq.append([el1 + numbers[pos + 1], pos + 1])
            dq.append([el1 - numbers[pos + 1], pos + 1])
    
    return answer