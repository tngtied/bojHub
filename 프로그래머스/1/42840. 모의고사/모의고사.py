def solution(answers):
    rights = [0, 0, 0]
    answer = []
    def second_guess (i):
        if i % 2 == 0:
            return 2
        if (i % 8 == 1):
            return 1
        if (i % 8 == 3):
            return 3
        if (i % 8 == 5):
            return 4
        if (i % 8 == 7):
            return 5
    def third_guess(i):
        cases = (3, 1, 2, 4, 5)
        return (cases[(i % 10) // 2])
    for i in range(len(answers)):
        if (answers[i] == i % 5 + 1):
            rights[0] += 1
        if (answers[i] == second_guess(i)):
            rights[1] += 1
        if (answers[i] == third_guess(i)):
            rights[2] += 1
    for i in range(3):
        if (rights[i] == max(rights)):
            answer.append(i + 1)

    return answer