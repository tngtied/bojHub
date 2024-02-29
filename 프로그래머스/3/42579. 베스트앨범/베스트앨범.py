def solution(genres, plays):
    answer = []
    play_map = {}
    genre_map = {}
    
    for i in range(len(genres)):
        if genres[i] in play_map:
            play_map[genres[i]].append((i, plays[i]))
            genre_map[genres[i]] += plays[i]
        else:
            play_map[genres[i]] = [(i, plays[i])]
            genre_map[genres[i]] = plays[i]
    sorted_genre = sorted(genre_map.items(), key = lambda x : genre_map[x[0]], reverse = True)
    print(str(sorted_genre))
    for genre in sorted_genre:
        play_map[genre[0]].sort(key = lambda x : x[1], reverse = True)
        sorted_songs = play_map[genre[0]]
        print(str(sorted_songs))
        song_num = min(len(sorted_songs), 2)
        if song_num == 2 and sorted_songs[0][1] == sorted_songs[1][1]:
            answer.append(min(sorted_songs[0][0], sorted_songs[1][0]))
            answer.append(max(sorted_songs[0][0], sorted_songs[1][0]))
        else:
            for i in range(song_num):
                answer.append(sorted_songs[i][0])
    return answer