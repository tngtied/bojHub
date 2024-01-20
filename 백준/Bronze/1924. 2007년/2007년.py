import sys
input = sys.stdin.readline
print = sys.stdout.write

x, y = map(int, input().split())
type_a = [ 1, 3, 5, 7, 8, 10, 12]
type_b = [4, 6, 9, 11]
type_c = [2]
count = (y - 1) % 7
for i in range(1, x):
    if (i in type_a):
        count += 31
    elif(i in type_b):
        count += 30
    else:
        count += 28
    count %= 7
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(days[count])