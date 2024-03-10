def solution(s):
    zeros = 0
    count = 0
    while True:
        if (s == '1'):
            break
        zeros += s.count("0")
        s = s.replace("0", "")
        print(type(bin(len(s))))
        s = bin(len(s))[2:]
        count += 1
    return [count, zeros]