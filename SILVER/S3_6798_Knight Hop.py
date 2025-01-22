from collections import deque


def bfs():
    visited = [[0] * 9 for _ in range(9)]

    queue = deque([(si, sj, 0)])
    visited[si][sj] = 1

    while queue:
        ci, cj, move = queue.popleft()

        if (ci, cj) == (ei, ej):
            return move

        for di, dj in (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1):
            ni, nj = ci + di, cj + dj

            if ni <= 0 or ni > 8 or nj <= 0 or nj > 8:
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))


si, sj = map(int, input().split())
ei, ej = map(int, input().split())

print(bfs())
