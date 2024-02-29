from collections import deque
def solution(s):
    answer = True
    ins = list(s)
    dq = deque()
    for i in range(len(ins)):
        if (ins[i] == "("):
            dq.append(True)
        else:
            if(len(dq)):
                dq.pop()
            else:
                return False
    if len(dq):
        return False

    return True