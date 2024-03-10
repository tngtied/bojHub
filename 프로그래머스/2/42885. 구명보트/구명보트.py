def solution(people, limit):
    people.sort()
    sp, ep = 0, len(people) - 1
    count = 0
    answer = 0
    while (count != len(people)):
        if (ep != sp and people[ep] + people[sp] <= limit):
            count += 2
            answer += 1
            ep -= 1
            sp += 1
        else:
            count += 1
            answer += 1
            ep -= 1
    return answer