from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]  # 안전 거리를 계산하기 위한 2차원 리스트
max_cnt = 0  # 안전 거리 최댓값

# 아기 상어의 좌표를 queue에 추가
queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j]:
            queue.append((i, j))
            visited[i][j] = 0  # visited를 0으로 저장

# bfs
while queue:
    i, j = queue.popleft()

    max_cnt = max(max_cnt, visited[i][j])  # 최댓값 여부 비교

    # 8방향을 탐색하여 이동이 가능한 지 체크
    for di, dj in (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1):
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))

print(max_cnt)  # 최댓값 출력