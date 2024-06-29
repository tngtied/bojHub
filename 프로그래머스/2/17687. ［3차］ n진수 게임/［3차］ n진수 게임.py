def solution(n, t, m, p):
    def get_n_num(num, base):
        digits = "0123456789ABCDEF"
        result = ""
        if num == 0:
            return "0"
        while (num > 0):
            num, mod = divmod(num, base)
            result += digits[mod]
        return result[::-1]
    
    answer = ''
    gameplay = ""
    j = 0
    while (len(gameplay)<= t * m):
        gameplay += get_n_num(j, n)
        j += 1
    print (gameplay)
    for i in range(t):
        answer += gameplay[p - 1]
        p += m
    return answer