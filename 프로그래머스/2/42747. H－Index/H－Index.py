def solution(citations):
    citations.sort(reverse = True)
    n = len(citations)
    for i in range(n):
        if (i + 1 > citations[i]):
            return i
    return n