def solution(n, words):
    answer = []
    wordset = set()
    count = 1
    round = 1
    flag = False
    for word in words:
        if flag:
            print(f"beforeword[-1]{beforeword[-1]} word[0]{word[0]}")
        if word in wordset or (flag and beforeword[-1] != word[0]):
            return [count, round]
        wordset.add(word)
        beforeword = word
        flag = True
        count += 1
        if count > n :
            round += 1
            count = 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return [0, 0]