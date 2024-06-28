def solution(n, k):
    dk = k
    dnums = [0]
    while dk // k <= n:
        dnums.append((n % dk) // (dk // k))
        n -= n % dk
        dk *= k
    dnums.append(0)
    nums = {}
    num = ""
    for i in range(len(dnums)):
        if dnums[len(dnums) - 1 - i] == 0:
            if (len(num) != 0):
                if int(num) in nums:
                    nums[int(num)] += 1
                else:
                    nums[int(num)] = 1
                num = ""
                print("~~")
        else:
            num += str(dnums[len(dnums) - 1 - i])
        print(num)
    # primes = [True for _ in range(max(nums) + 1)]
    # primes[0] = False
    # primes[1] = False
    # for i in range(2, max(nums) + 1):
    #     if primes[i]:
    #         num = i + i
    #         while num <= max(nums):
    #             primes[num] = False
    #             num += i
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    answer = 0
    for num in nums:
        if is_prime(num):
            print(num)
            answer += nums[num]
    print(dnums)
    print(nums)

        
    return answer