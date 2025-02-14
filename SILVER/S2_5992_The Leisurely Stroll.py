"""
헛간(1)부터 이어져있는 길 중 가장 긴 길이 출력
"""

from collections import deque

p = int(input())
path = [[] for _ in range(p + 1)]
visited = [0] * (p + 1)
max_length = 0

for _ in range(p - 1):
    c, d1, d2 = map(int, input().split())

    if d1:
        path[c].append(d1)
    if d2:
        path[c].append(d2)

queue = deque([(1, 1)])
visited[1] = 1

while queue:
    now, length = queue.popleft()

    max_length = max(length, max_length)

    for p in path[now]:
        if not visited[p]:
            visited[p] = 1
            queue.append((p, length + 1))

print(max_length)
