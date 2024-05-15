import heapq
def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city_ in cities:
        flag = False
        city = city_.lower()
        for i, cached_city in enumerate(cache):
            if cached_city == city:
                cache.pop(i)
                flag = True
                break
        cache.append(city)
        if flag:
            answer += 1
        else:
            answer += 5
        if len(cache) > cacheSize:
            cache.pop(0)
    return answer