def solution(k, tangerine):
    n = max(tangerine) + 1
    size = [[0, i] for i in range(n)]
    for t in tangerine:
        size[t][0] += 1
    size.sort()
    count = 0
    answer = 0
    for i in range(n):
        count += size[n - i - 1][0]
        answer += 1
        if count >= k:
            break
    return answer