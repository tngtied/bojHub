def solution(brown, yellow):
    answer = []
    for col in range(1, yellow + 1):
        if yellow % col == 0:
            row = yellow // col
            print("row %d col %d calculation %d" % (row, col, row * 2 + col * 2 + 4))
            if (row * 2 + col * 2 + 4 == brown):
                return [row + 2, col + 2]
    return answer