import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))

queue = deque()
queue.append((a_list[0], 0))

for i in range(N):
    while queue and queue[-1][0] > a_list[i]:
        queue.pop()
    while queue and queue[0][1] < i - L + 1:
        queue.popleft()
    queue.append((a_list[i], i))

    print(queue[0][0], end=' ')