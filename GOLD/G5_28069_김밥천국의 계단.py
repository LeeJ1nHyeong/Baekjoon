from collections import deque


def bfs():
    visited = [0] * (n + 1)

    queue = deque([(0, 0)])
    visited[0] = 1

    while queue:
        now, cnt = queue.popleft()

        if now == n and cnt <= k:
            return "minigimbob"

        if now + 1 <= n and not visited[now + 1]:
            visited[now + 1] = 1
            queue.append((now + 1, cnt + 1))

        if now + now / 2 <= n and not visited[now + now // 2]:
            visited[now + now // 2] = 1
            queue.append((now + now // 2, cnt + 1))

    return "water"


n, k = map(int, input().split())

print(bfs())
