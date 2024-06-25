def solution(n,a,b):
    def next_number(number):
        if number % 2 == 1:
            number += 1
        return number//2
    answer = 0
    while a!=b:
        a = next_number(a)
        b = next_number(b)
        answer += 1
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer