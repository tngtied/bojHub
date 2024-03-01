def solution(sizes):
    answer = 0
    row, col = max(sizes[0][0], sizes[0][1]), min(sizes[0][0], sizes[0][1])
    for i in range(1, len(sizes)):
        row = max(row, max(sizes[i][0], sizes[i][1]))
        col = max(col, min(sizes[i][0], sizes[i][1]))
    return row * col