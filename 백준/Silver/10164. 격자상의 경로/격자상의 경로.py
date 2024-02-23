import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m, k = map(int, input().split())
if k == 0:
    kx, ky = 0, 0
elif (k % m == 0):
    kx = k // m - 1
    ky = m - 1
else:
    kx, ky = k // m, k % m - 1
dp = [[0 for __ in range(m)] for _ in range(n)]
# 세로, 가로
dp[0][0] = 1
dxy = [(0, -1), (-1, 0)]
def solution(sx, sy, ex, ey):
    for j in range(sy, ey + 1):
        for i in range(sx, ex + 1):
            for d in dxy:
                px, py = i + d[0], j + d[1]
                if (px < sx or py < sy):
                    continue
                dp[i][j] += dp[px][py]
solution(0, 0, kx, ky)
solution(kx, ky, n - 1, m - 1)
print ("%d" % dp[n - 1][m - 1])