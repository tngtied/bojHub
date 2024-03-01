def solution(k, dungeons):
    visit = [False] * (len(dungeons))
    def solve(hp, dungeons, count):
        
        result = count
        for i in range(len(dungeons)):
            if dungeons[i][0] <= hp and not visit[i]:
                visit[i] = True
                result = max(result, solve(hp - dungeons[i][1], dungeons, count + 1))
                visit[i] = False
        return result
    return solve(k, dungeons, 0)