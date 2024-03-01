from itertools import permutations
def primes(max_val):
    arr = [1] * (max_val + 1)
    arr[0], arr[1] = -1, -1
    for i in range(2, max_val + 1):
        if arr[i] == 0:
            continue
        j = 2
        while (i * j <= max_val):
            arr[i * j] = 0
            j += 1
    return arr
def solution(numbers):
    numbers = list(numbers)
    candidates = []
    for i in range(len(numbers)):
        candidates += permutations(numbers, i + 1)
    numbers = list(map(int, map(''.join, candidates)))
    max_number = max(numbers)
    answer = 0
    prime_numbers = primes(max_number)
    for number in numbers:
        if prime_numbers[number] == 1:
            answer += 1
            prime_numbers[number] += 1   
    return answer