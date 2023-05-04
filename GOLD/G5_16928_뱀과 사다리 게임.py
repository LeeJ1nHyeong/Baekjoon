import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ladder = [0 for _ in range(101)]
snake = [0 for _ in range(101)]
visited = [0 for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    ladder[u] = v

queue = deque()
queue.append(1)

while queue:
    now = queue.popleft()
    for i in range(1, 7):
        next = now + i
        if next <= 100:
            if ladder[next]:
                next = ladder[next]
            if snake[next]:
                next = snake[next]
            if not visited[next]:
                visited[next] = visited[now] + 1
                queue.append(next)

    if 100 in queue:
        break

print(visited[100])