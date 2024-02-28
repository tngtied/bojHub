def solution(genres, plays):
    answer = []
    hashmap = {}
    total_dict = {}
    for i in range(len(genres)):
        if (genres[i] in hashmap):
            hashmap[genres[i]].append((plays[i], i))
            total_dict[genres[i]] += plays[i]
        else:
            hashmap[genres[i]] = [(plays[i], i)]
            total_dict[genres[i]] = plays[i]
    sorted_genre = sorted(total_dict.items(), key = lambda x: total_dict[x[0]], reverse = True)
    for gen in sorted_genre:
        print(">>gen %s" % str(gen))
        key_genre = gen[0]
        hashmap[key_genre].sort(reverse = True)
        if (len(hashmap[key_genre]) > 1 and hashmap[key_genre][0][0] == hashmap[key_genre][1][0]):
            answer.append(min(hashmap[key_genre][0][1], hashmap[key_genre][1][1]))
            answer.append(max(hashmap[key_genre][0][1], hashmap[key_genre][1][1]))
        else:
            for j in range(min(len(hashmap[key_genre]), 2)):
                answer.append(hashmap[key_genre][j][1])    
    return answer