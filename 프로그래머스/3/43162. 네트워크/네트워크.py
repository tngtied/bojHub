from collections import deque

def solution(n, computers):
    visit = [False for _ in range(n)]
    def bfs(i):
        dq = deque()
        dq.append(i)
        visit[i] = True
        while (dq):
            x = dq.popleft()
            for y in range(len(computers[x])):
                if not visit[y] and computers[x][y] == 1:
                    visit[y] = True
                    dq.append(y)
    answer = 0
    for i in range(n):
        if not visit[i]:
            bfs(i)
            print(i)
            print(visit)
            answer += 1
    return answer

        