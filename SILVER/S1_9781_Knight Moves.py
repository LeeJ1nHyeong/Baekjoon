from collections import deque


def bfs():
    visited = [[0] * m for _ in range(n)]
    queue = deque()

    # 나이트의 위치를 찾아 방문 표시 후 queue에 추가
    for i in range(n):
        for j in range(m):
            if board[i][j] == "K":
                visited[i][j] = 1
                queue.append((i, j, 0))
                break

    # bfs 진행
    while queue:
        ci, cj, move = queue.popleft()

        if board[ci][cj] == "X":
            return move

        for di, dj in (1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1):
            ni, nj = ci + di, cj + dj

            ## 탐색 제외 목록
            # 범위 밖을 벗어난 지역
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            # 벽인 지역
            if board[ni][nj] == "#":
                continue
            # 방문 지역
            if visited[ni][nj]:
                continue

            # 방문표시 후 queue에 추가
            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))

    return -1  # while문이 종료됐다면 목표 위치에 도달을 못한다는 뜻이므로 -1 return


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

print(bfs())
