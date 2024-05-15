def solution(n, stations, w):
    answer = 0
    s = 0
    for station in stations:
        t = station - 1 - w

        answer += (t - s) // (2 * w + 1)
        if ((t - s) % (2 * w + 1) != 0):
            answer += 1
        print(answer)
        s = station + w
        if s >= n:
            break
    if s < n:
        answer += (n - s) // (2 * w + 1)
        if ((n - s) % (2 * w + 1) != 0):
            answer += 1
    
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer