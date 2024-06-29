def solution(numbers):
    import heapq
    answer = [-1 for _ in range(len(numbers))]
    hq = []
    for i in range(len(numbers)):
        # print(f"numbers[i] {numbers[i]}, hq {hq}")

        while len(hq):
            number, pos = heapq.heappop(hq)
            if number < numbers[i]:
                answer[pos] = numbers[i]
            else:
                heapq.heappush(hq, [number, pos])
                break
        heapq.heappush(hq, [numbers[i], i])
    # if hq:
    #     number, pos = heapq.heappop(hq)
    #     while hq and number < numbers[i]:
    #         answer[pos] = numbers[i]
    #         number, pos = heapq.heappop(hq)
    #     heapq.heappush(hq, [number, pos])
    
    return answer