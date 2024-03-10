from collections import deque
def solve(s, sp):
    opens = ('(', '{', '[')
    closes = (')', '}', ']')
    dq = deque()
    charList = list(s)
    for i in range(len(s)):
        index = (sp + i) % len(s)
        if charList[index] in opens:
            dq.append(charList[index])
        else:
            if len(dq) == 0:
                print("분기 A")
                return False
            popped = dq.pop()
            flag = False
            for j in range(3):
                if opens[j] == popped and closes[j] == charList[index]:
                    flag = True
                    break
            if not flag:
                print("분기 B")
                return False
    if (len(dq) == 0):
        return True
    return False

def solution(s):
    count = 0
    for i in range(len(s) - 1):
        if (solve (s, i)):
            count += 1
    return count
        