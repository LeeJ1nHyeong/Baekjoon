from collections import deque

while True:
    n, m = map(int, input().split())

    if (n, m) == (0, 0):
        break

    board = [list(input()) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    ans = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == "*":
                continue

            if visited[i][j]:
                continue

            queue = deque([(i, j)])
            visited[i][j] = 1

            while queue:
                ci, cj = queue.popleft()

                # 현재 위치 기준 8방향 탐색하여 연속되는 영역 탐색
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                    ni, nj = ci + di, cj + dj

                    if ni < 0 or ni == n or nj < 0 or nj == m:
                        continue

                    if board[ni][nj] == "*":
                        continue

                    if visited[ni][nj]:
                        continue

                    # 조건에 만족하는 위치라면 방문 표시 후 queue에 좌표 추가
                    visited[ni][nj] = 1
                    queue.append((ni, nj))

            # bfs 종료 후 영역 개수 1 추가
            ans += 1

    print(ans)
