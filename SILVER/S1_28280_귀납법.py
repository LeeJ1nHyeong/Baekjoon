from collections import deque


def bfs():
    visited = [0] * 4000001
    queue = deque([(1, 0)])
    visited[1] = 1

    while queue:
        now, cnt = queue.popleft()

        if now == k:
            return cnt

        if now - 1 > 0 and not visited[now - 1]:
            visited[now - 1] = 1
            queue.append((now - 1, cnt + 1))
        if now * 2 <= 4000000 and not visited[now * 2]:
            visited[now * 2] = 1
            queue.append((now * 2, cnt + 1))

    return "Wrong proof!"


t = int(input())

for _ in range(t):
    k = int(input())
    print(bfs())
