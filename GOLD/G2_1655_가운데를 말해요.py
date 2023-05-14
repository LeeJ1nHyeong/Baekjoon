import sys
import heapq
input = sys.stdin.readline

N = int(input())
maxHeap = []
minHeap = []

mid = int(input())
print(mid)

for _ in range(2, N + 1):
    num = int(input())
    if mid < num:
        heapq.heappush(minHeap, num)
    else:
        heapq.heappush(maxHeap, - num)

    if len(minHeap) - len(maxHeap) == 2:
        heapq.heappush(maxHeap, -mid)
        mid = heapq.heappop(minHeap)
    if len(maxHeap) - len(minHeap) == 2:
        heapq.heappush(minHeap, mid)
        mid = -heapq.heappop(maxHeap)

    if len(maxHeap) <= len(minHeap):
        print(mid)
    if len(maxHeap) > len(minHeap):
        print(-maxHeap[0])