import sys
input = sys.stdin.readline
print = sys.stdout.write

def sublist_sum(l, r):
    if (l == 0):
        left = 0
    else:
        left = accumul_list[l - 1] 
    return accumul_list[r] - left

def repetitive():
    dp[0] = seq[0]
    for i in range(1, N):
        cand = float("INF")
        for j in range(i + 1):
            if (j - 1 < 0):
                temp = 0
            else:
                temp = dp[j - 1]
            cand = min (cand, sublist_sum(j, i) - temp)
        dp[i] = cand
    return dp[N - 1]
   
N = int(input())

dp = [0] * N
accumul_list = [0] * N
def run(seq):
    accumul_list[0] = seq[0]
    for i in range(N):
        if (i != 0):
            accumul_list[i] = accumul_list[i - 1] + seq[i]
    ans = repetitive()
    return ans


for i in range(3):
    seq = list(map(int, input().split()))
    ans = run(seq)
    if (ans == 0):
        print("D\n")
    elif (ans < 0):
        print("A\n")
    else:
        print("B\n")