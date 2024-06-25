def solution(want, number, discount):
            
    answer = 0
    def check(w_dict, d_dict):
        for w in w_dict:
            if w not in d_dict or w_dict[w] > d_dict[w]:
                return False
        return True
    want_dict = dict()
    discount_dict = dict()
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    for i in range(len(discount)):
        if i >= 10:
            discount_dict[discount[i - 10]] -= 1
        if discount[i] in discount_dict:
            discount_dict[discount[i]] += 1
        else:
            discount_dict[discount[i]] = 1
        # print(str(want_dict) + str(discount_dict))
        if check(want_dict, discount_dict):
            answer += 1

    return answer