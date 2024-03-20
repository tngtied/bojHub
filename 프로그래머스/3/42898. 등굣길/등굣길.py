def solution(m, n, puddles):
    board = [[True for j in range(m)] for i in range(n)]
    for x, y in puddles:
        board[y - 1][x - 1] = False
    dp = [[0 for __ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                continue
            for dy, dx in ((0, -1), (-1, 0)):
                if (i + dy >= 0 and j + dx >= 0):
                    dp[i][j] += dp[i + dy][j + dx] 
                    dp[i][j] %= 1000000007
    # print(str(dp))
    return dp[n - 1][m - 1] % 1000000007