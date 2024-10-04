from collections import deque


def bfs():
    visited = [[0] * c for _ in range(r)]
    queue = deque()

    # 시작 지점 탐색
    for i in range(r):
        for j in range(c):
            if board[i][j] == "B":
                visited[i][j] = 1
                queue.append((i, j, 0))

    # bfs 진행
    while queue:
        ci, cj, move = queue.popleft()

        # 목표 지점에 도착했다면 이동 횟수 return
        if board[ci][cj] == "C":
            return move

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == r or nj < 0 or nj == c:
                continue

            if board[ni][nj] == "*":
                continue

            if visited[ni][nj]:
                continue

            # 이동 조건을 만족하는 위치에 대해 방문 표시 후 queue에 좌표 추가
            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

print(bfs())
