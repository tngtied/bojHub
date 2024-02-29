def solution(numbers):

    numbers=list(map(str,numbers))
    numbers.sort(key = lambda x : x * 5, reverse= True)
    # print("%s" % str(numbers))
    if (numbers[0][0] == "0"):
        return "0"
    answer = ''.join(numbers)
    
    return answer