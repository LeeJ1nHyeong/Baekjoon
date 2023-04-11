import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

second = 0
visited = [False] * 100001
queue = deque()
temp = []
queue.append(N)

while queue:
    if N == K:
        second = 0
        break

    now = queue.popleft()
    visited[now] = True

    if 0 <= now - 1 <= 100000 and not visited[now - 1]:
        if now - 1 == K:
            second += 1
            break
        else:
            temp.append(now - 1)
    if 0 <= now + 1 <= 100000 and not visited[now + 1]:
        if now + 1 == K:
            second += 1
            break
        else:
            temp.append(now + 1)
    if 0 <= 2 * now <= 100000 and not visited[2 * now]:
        if 2 * now == K:
            second += 1
            break
        else:
            temp.append(2 * now)

    if not queue:
        queue = deque(set(temp))
        temp.clear()
        second += 1

print(second)