from collections import deque
def solution(priorities, location):
    prior_with_index = []
    dq = deque()
    for i in range(len(priorities)):
        prior_with_index.append((priorities[i], i))
        dq.append(i)
    count = 1
    prior_with_index.sort(reverse = True)
    print(str(prior_with_index))
    for p in prior_with_index:
        el = dq.popleft()
        while(priorities[el] != p[0]):
            dq.append(el)
            el = dq.popleft()
        if (el == location):
            return count
        count += 1
    
    answer = 0
    return answer