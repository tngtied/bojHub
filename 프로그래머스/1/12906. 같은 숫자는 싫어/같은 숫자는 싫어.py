from collections import deque
def solution(arr):
    answer = []
    dq = deque()
    dq.append(arr[0])
    for i in range(1, len(arr)):
        last = dq.pop()
        el = arr[i]
        if (last == el):
            dq.append(last)
        else:
            dq.append(last)
            dq.append(el)
    while (len(dq)):
        answer.append(dq.popleft())
    print('Hello Python')
    return answer