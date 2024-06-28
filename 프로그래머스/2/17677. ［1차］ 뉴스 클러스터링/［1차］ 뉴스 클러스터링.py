def solution(str1, str2):
    def get_dict(string):
        word = ""
        result = {}
        for i in range(len(string) - 1):
            c1, c2 = string[i], string[i + 1]
            if ('a' <= c1 <= 'z' or 'A' <= c1 <= 'Z') and ('a' <= c2 <= 'z' or 'A' <= c2 <= 'Z'):
                word = c1.lower() + c2.lower()
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
        return result
    dict1 = get_dict(str1)
    dict2 = get_dict(str2)
    print(f"dict1 {dict1}")
    print(f"dict2 {dict2}")
    left = 0
    right = 0
    for word in dict1:
        if word in dict2:
            left += min(dict1[word], dict2[word])
            right += max(dict1[word], dict2[word])
        else:
            right += dict1[word]
    for word in dict2:
        if word not in dict1:
            right += dict2[word]
    print(f"left{left} right{right}")
    answer = 65536
    if right != 0:
        answer = left / right * 65536
    return int(answer)