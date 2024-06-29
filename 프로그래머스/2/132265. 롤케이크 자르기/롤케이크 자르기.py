def solution(topping):
    left = set()
    lcount = 0
    right = {}
    rcount = 0
    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1
            rcount += 1
    answer = 0
    for t in topping:
        right[t] -= 1
        left.add(t)
        if right[t] == 0:
            rcount -= 1
        if rcount == len(left):
            answer += 1
    return answer