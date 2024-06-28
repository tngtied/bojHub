def solution(n, left, right):
    sx, sy = left % n, left // n
    tx, ty = right % n, right // n
    answer = []
    for y in range(sy, ty + 1):
        lx = 0 if y != sy else sx
        rx = n - 1 if y != ty else tx
        print(f"y {y}, lx {lx}, rx{rx}")
        answer += [max(x, y) + 1 for x in range(lx, rx + 1)]
    
    return answer