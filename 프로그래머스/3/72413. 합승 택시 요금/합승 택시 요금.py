from collections import deque
def solution(n, s, c, d, fares):
    def bfs(a, edges):
        dist = dict()
        dq = deque()
        dq.append(a)
        dist[a] = 0
        n = len(edges)
        i = 0
        while len(dq):
            i += 1
            l = dq.popleft()
            for r, d in edges[l]:
                if r not in dist or dist[r] > dist[l] + d:
                    dist[r] = dist[l] + d
                    dq.append(r)
        return dist
    
    reachable = [[-1, -1] for i in range(n + 1)]
    edges = dict()
    for i in range(n + 1): edges[i] = []
    for a, b, dist in fares:
        edges[a].append([b, dist])
        edges[b].append([a, dist])
    
    s_dict = bfs(s, edges)
    answer = s_dict[c] + s_dict[d]
    
    for i in s_dict:
        if i == s:
            continue
        t_dict = bfs(i, edges)
        answer = min(answer, s_dict[i] + t_dict[c] + t_dict[d])
    
    return answer