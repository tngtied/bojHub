def solution(msg):
    word_dict = {}
    for c in range(ord("A"), (ord('Z')+ 1)):
        word_dict[chr(c)] = (c - ord('A')+ 1)
    # print(word_dict)
    i = 0
    dict_count = 27
    current_word = ""
    answer = []
    while i < len(msg):
        nword = current_word + msg[i]
        # print(nword)
        # print(nword in word_dict)
        if i == len(msg) - 1:
            if nword in word_dict:
                # print(nword)
                answer.append(word_dict[nword])
            else:
                # print(current_word)
                answer.append(word_dict[current_word])
                answer.append(word_dict[msg[i]])
        elif nword in word_dict:
            current_word = nword
        else:
            # print(current_word)
            answer.append(word_dict[current_word])
            word_dict[nword] = dict_count
            dict_count += 1
            current_word = ""
            i -= 1
        i += 1
    
    return answer