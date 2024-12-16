from collections import deque


def bfs():
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0, 0)])
    visited[0][0] = 1

    while queue:
        ci, cj, move = queue.popleft()

        if (ci, cj) == (i, j):
            return move

        for di, dj in (1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))

    return "NEVAR"


n, m, i, j = map(int, input().split())
i -= 1
j -= 1

print(bfs())
