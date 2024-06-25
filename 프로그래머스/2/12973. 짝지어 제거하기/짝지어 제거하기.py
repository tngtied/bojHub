import heapq
def solution(s):
    stack = []
    for e in s:
        if stack and stack[-1] == e:
            stack.pop()
        else:
            stack.append(e)
    return int(not stack)