def solution(n, edge):
    from collections import deque
    shortest_path = {1 : 0}
    edge_dict = {}
    length_count = {}
    for s, t in edge:
        if s not in edge_dict:
            edge_dict[s] = []
        edge_dict[s].append(t)
        if t not in edge_dict:
            edge_dict[t] = []
        edge_dict[t].append(s)
    dq = deque()
    dq.append([1, 0])
    length_count = {0 : 1}

    while dq:
        node, length = dq.popleft()
        for next_node in edge_dict[node]:
            if next_node not in shortest_path or shortest_path[next_node] > length + 1:
                if next_node in shortest_path:
                    length_count[shortest_path[next_node]] -= 1
                if length + 1 not in length_count:
                    length_count[length + 1] = 0
                shortest_path[next_node] = length + 1
                length_count[length + 1] += 1
                dq.append([next_node, length + 1])
    answer = 0
    max_length = 0
    for key, value in length_count.items():
        if key > max_length:
            key = max_length
            answer = value
        
    
    return answer