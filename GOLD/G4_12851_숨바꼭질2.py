import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

cnt = 0
visited = [0] * 100001
queue = deque()
queue.append(N)

while queue:
    now = queue.popleft()
    if now == K:
        cnt += 1
        if now == N:
            break

    for i in [now - 1, now + 1, 2 * now]:
        if 0 <= i <= 100000:
            if visited[i] == 0 or visited[i] == visited[now] + 1:
                visited[i] = visited[now] + 1
                queue.append(i)

print(visited[K])
print(cnt)