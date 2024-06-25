def solution(n):
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        fibonacci.append((fibonacci[i - 2] + fibonacci[i - 1]) % 1234567)
    return fibonacci[-1]