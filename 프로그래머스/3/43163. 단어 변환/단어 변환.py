def is_peer(word_a, word_b):
    list_a = list(word_a)
    list_b = list(word_b)
    diff = 0
    for i in range(len(list_a)):
        if list_a[i] != list_b[i]:
            diff += 1
        if diff > 1:
            return False
    return True
import heapq
def solution(begin, target, words):
    if not(target in words):
        return 0
    edges = dict()
    words.append(begin)
    visit = dict()
    hq = []
    for i in range(len(words)):
        edges[words[i]] = []
        visit[words[i]] = False
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_peer(words[i], words[j]):
                edges[words[i]].append(words[j])
                edges[words[j]].append(words[i])
    print(edges)
    answer = 0
    hq.append([0, begin])
    visit[begin] = True
    while hq:
        count, sword = heapq.heappop(hq)
        for tword in edges[sword]:
            if not visit[tword]:
                if tword == target:
                    return count + 1
                if tword != begin: 
                    heapq.heappush(hq, [count + 1, tword])
                visit[tword] = True
    return answer