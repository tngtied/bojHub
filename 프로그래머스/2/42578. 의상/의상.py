def solution(clothes):
    hashmap = {}
    for c in clothes:
        if (c[1] in hashmap):
            hashmap[c[1]] += 1
        else:
            hashmap[c[1]] = 1
    answer = 1
    for c in hashmap:
        answer *= (hashmap[c] + 1)
    return answer - 1