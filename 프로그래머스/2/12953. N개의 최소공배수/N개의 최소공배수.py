def solution(arr):
    candidate = max(arr)
    while True:
        flag = False
        for el in arr:
            if candidate % el != 0:
                flag = True
                break
        if flag:
            candidate += max(arr)
        else:
            answer = candidate
            break
    return answer