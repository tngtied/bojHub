from collections import deque
def solution(prices):
    dq = deque()
    dq_len = 0
    answer = [-1 for _ in range(len(prices))]
    index = 0
    for p in prices:
        temp = dq_len
        for i in range(temp):
            el = dq.popleft()
            if (el[0] <= p):
                dq.append((el[0], el[1] + 1, el[2]))
                # price, duration, index
            else:
                answer[el[2]] = el[1] + 1
                dq_len -= 1
        dq.append((p, 0, index))
        index += 1
        dq_len += 1
    for i in range(dq_len):
        el = dq.popleft()
        answer[el[2]] = el[1] 
    return answer