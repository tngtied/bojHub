def solution(n):
    dp = [1]
    for i in range(1, n + 1):
        temp = 0
        if (i - 2 >= 0):
            temp += dp[i - 2]
        if (i - 1 >= 0):
            temp += dp[i - 1]
        dp.append(temp % 1234567)
    print(dp)
    return dp[-1]