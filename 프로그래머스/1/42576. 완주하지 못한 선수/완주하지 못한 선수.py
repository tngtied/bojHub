def solution(participant, completion):
    hashmap = {}
    for p in participant:

        if (p in hashmap):
            hashmap[p] += 1
        else:
            hashmap[p] = 1
    for c in completion:
        hashmap[c] -= 1
    for el in hashmap:
        if (hashmap[el] > 0):
            return el
        