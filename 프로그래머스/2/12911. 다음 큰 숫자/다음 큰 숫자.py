def solution(n):
    def how_many_ones(number):
        result = 1 if number % 2 == 1 else 0
        divider = 4
        while True:
            if ((number % divider) - (number % (divider / 2))) / (divider / 2) == 1:
                result += 1
            divider *= 2
            if number % (divider / 2) == number:
                break
        return result
    n_ones = how_many_ones(n)
    while True:
        n += 1
        if how_many_ones(n) == n_ones:
            return n