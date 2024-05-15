import heapq
def solution(n, s):
    if n > s:
        return [-1]
    answer = [s//n for _ in range(n)]
    for i in range(s % n):
        answer[n - 1 - i] += 1
    return answer