import sys
input = sys.stdin.readline
print = sys.stdout.write
tc = int(input())
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [arr[0]]
    result = dp[0]
    for i in range(1, len(arr)):
        dp.append(max(0, dp[i - 1]) + arr[i])
        result = max(dp[i], result)
    print("%d\n" % result)
for t in range(tc):
    solution()