import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write
def solution():
    n = int(input())
    min_heap = []
    max_heap = []
    visit = {}
    for _ in range(n):
        command, k = input().strip().split()
        k = int(k)
        if (command == "I"):
            heapq.heappush(max_heap, (-k, _))
            heapq.heappush(min_heap, (k, _))
            visit[_] = 1
        else:

            if (k == -1):
                if (min_heap):
                    visit[heapq.heappop(min_heap)[1]] = 0
            else:
                if (max_heap):
                    visit[heapq.heappop(max_heap)[1]] = 0
        while min_heap and visit[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        while max_heap and visit[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
    if (len(min_heap) == 0):
        print("EMPTY\n")
    else:
        print("%d %d" % (-max_heap[0][0], min_heap[0][0]))
        print("\n")
tc = int(input())
for _ in range(tc):
    solution()