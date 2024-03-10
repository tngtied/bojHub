def solution(arr):
    sp = max(arr)
    while True:
        flag = False
        for el in arr:
            if sp % el != 0:
                flag = True
                break
        if (flag):
            sp += 1
        else:
            break
    return sp