def solution(n):
    dp = [0 for _ in range(n)]
    sp = 0
    count = 0
    for i in range(1, n + 1):
        for j in range(sp, i):
            dp[j] += i
            if (dp[j] > n):
                sp = j + 1
            elif (dp[j] == n):
                count += 1
                sp = j + 1
    return count