import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:

        el1 = heapq.heappop(scoville)
        if (el1 >= K):
            return answer
        if (len(scoville) < 1):
            return -1
        el2 = heapq.heappop(scoville)
        heapq.heappush(scoville, el1 + (el2 * 2))
        answer += 1
    return answer