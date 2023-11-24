from collections import deque
def solution(alp, cop, problems):
    dp = []
    maxalp = max(problems, key = lambda x: x[0])[0]
    maxcop = max(problems, key = lambda x: x[1])[1]
    alp = min(alp, maxalp)
    cop = min(cop, maxcop)
    inf = float("inf")
    for i in range(maxalp + 1):
        dp.append([inf] * (maxcop + 1))
    dp[alp][cop] = 0
    problems.sort(key = lambda x: (x[0], x[1]))
    for i in range(alp, maxalp + 1):
        for j in range(cop, maxcop + 1):
            if (i < maxalp):
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            if (j < maxcop):
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            for p in problems:
                if (p[0] <= i and p[1] <= j):
                    nexti = min(i + p[2], maxalp)
                    nextj = min(j + p[3], maxcop)
                    dp[nexti][nextj] = min(dp[nexti][nextj], dp[i][j] + p[4])
                elif (p[0] > i and p[1] > j):
                    break
    # while q:
    #     cur_alp, cur_cop = q.pop()
        
    # print(str(problems))


    return dp[maxalp][maxcop]
print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))