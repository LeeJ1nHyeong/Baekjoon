''' 문제 설명

불난 곳(B)에서 호수(L)까지 이동할 수 있는 경로 중 최단 거리
바위(R)가 있는 곳은 이동 불가

'''

from collections import deque


def bfs():
    while queue:
        ci, cj, move = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == 10 or nj < 0 or nj == 10:
                continue

            if board[ni][nj] == "L":
                return move

            if board[ni][nj] == "R":
                continue

            if visited[ni][nj]:
                continue

            # 이동 가능한 위치에 대해 방문 표시 후 queue에 좌표 추가
            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))


board = [list(input()) for _ in range(10)]
visited = [[0] * 10 for _ in range(10)]

queue = deque()

# 불난 곳의 좌표를 방문 표시 후 queue에 추가
for i in range(10):
    for j in range(10):
        if board[i][j] == "B":
            visited[i][j] = 1
            queue.append((i, j, 0))

print(bfs())
