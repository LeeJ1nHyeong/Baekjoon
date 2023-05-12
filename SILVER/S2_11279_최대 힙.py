import sys
import heapq
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    x = int(input())
    if not x:
        if not queue:
            print(0)
        else:
            print(abs(heapq.heappop(queue)))
    else:
        heapq.heappush(queue, -x)