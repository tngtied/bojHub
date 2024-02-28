def solution(phone_book):
    phone_book.sort(key = len)
    min_len = len(phone_book[0])
    hashmap = {}
    for i in range(len(phone_book)):
        hashmap[phone_book[i]] = True
        for j in range(min_len, len(phone_book[i])):
            if phone_book[i][0:j] in hashmap:
                return False
    return True