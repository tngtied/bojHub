import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
bottom = []
for i in range(n):
    j = int(input()) - 1
    bottom.append(j)
visit = [-1] * n
answer = []
visited_list = []
snode = [-1] * n
count = 0
def dfs(s, sp):
    global count
    if (visit[bottom[s]] == -1):
        visit[bottom[s]] = count
        count += 1
        visited_list.append(bottom[s])
        snode[bottom[s]] = sp
        dfs(bottom[s], sp)
    elif (snode[bottom[s]] == sp):
        for i in range(visit[bottom[s]], visit[s] + 1):
            answer.append(visited_list[i])

for i in range(n):
    if (visit[i] == -1):
        snode[i] = i
        visit[i] = count
        count += 1
        visited_list.append(i)
        dfs(i, i)
print("%d\n" % len(answer))
answer.sort()
for a in answer:
    print("%d\n" % (a + 1))
