def solution(word):
    from collections import deque
    dq = deque()
    dq.append([["A"], 1])
    vowels = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' :4, 0:'A', 1:'E', 2:'I', 3:'O', 4:'U'}
    while dq:
        word_list, count = dq.popleft()
        if ''.join(word_list) == word:
            return count
        if len(word_list) < 5:
            dq.append([word_list + ['A'], count + 1])
        else:
            for i in range(5):
                if word_list[4 - i] != 'U':
                    word_list[4 - i] = vowels[vowels[word_list[4 - i]] + 1]
                    break
                else:
                    word_list.pop(4 - i)
            if word_list != []:
                dq.append([word_list, count + 1])
    # print(make_word("", 0))
    return answer