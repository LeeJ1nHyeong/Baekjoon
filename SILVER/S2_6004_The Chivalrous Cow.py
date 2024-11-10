from collections import deque


def bfs():
    queue = deque()

    # 시작지점 K 탐색
    for i in range(n):
        for j in range(m):
            if board[i][j] == "K":
                queue.append((i, j, 0))
                visited[i][j] = 1

    while queue:
        ci, cj, move = queue.popleft()

        if board[ci][cj] == "H":
            return move
        
        # 체스의 나이트 이동 8방향으로 탐색
        for di, dj in (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if board[ni][nj] == "*":
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))


m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

print(bfs())
