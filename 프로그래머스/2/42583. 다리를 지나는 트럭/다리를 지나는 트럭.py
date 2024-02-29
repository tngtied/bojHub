from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_index = 0
    answer = 0
    dq = deque()
    dq_len = 0
    cur_weight = 0
    while True:
        for i in range(dq_len):
            el = dq.popleft()
            if (el[0] == 1):
                cur_weight -= el[1]
                dq_len -= 1
            else:
                dq.append((el[0] - 1, el[1]))
        if (truck_index < len(truck_weights) and cur_weight + truck_weights[truck_index] <= weight):
            dq.append((bridge_length, truck_weights[truck_index]))
            cur_weight += truck_weights[truck_index]
            dq_len += 1
            truck_index += 1
        answer += 1
        if (dq_len == 0):
            break
    return answer