def solution(citations):
    citations.sort(reverse = True)
    n = len(citations)
    for i in range(n):
        print("citations[i] %d, i + 1 %d, n - 1 - i %d" % (citations[i] , i + 1, n - 1 - i))
        if (i + 1 > citations[i] ):
            return i
    return n