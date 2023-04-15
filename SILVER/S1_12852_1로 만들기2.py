import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque([[N]])
num_list = []

while queue:
    now = queue.popleft()
    x = now[0]

    if x == 1:
        num_list = now
        break

    if x % 3 == 0:
        queue.append([x // 3] + now)
    if x % 2 == 0:
        queue.append([x // 2] + now)

    queue.append([x - 1] + now)

num_list.sort(reverse=True)
print(len(num_list) - 1)
print(*num_list)