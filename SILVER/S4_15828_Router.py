from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

while True:
    packet = int(input())

    if packet == -1:
        if queue:
            print(*queue)
        else:
            print("empty")

        break

    elif packet:
        if len(queue) < n:
            queue.append(packet)

    elif not packet:
        queue.popleft()
