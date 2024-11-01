from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

island = 0  # 섬의 개수
for i in range(n):
    for j in range(m):
        if not board[i][j] or visited[i][j]:
            continue

        queue = deque([(i, j)])
        visited[i][j] = 1

        while queue:
            ci, cj = queue.popleft()

            # 현재 위치와 인접해있는 땅(대각선 포함) 탐색
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == m:
                    continue

                if not board[ni][nj]:
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                queue.append((ni, nj))

        island += 1

print(island)
