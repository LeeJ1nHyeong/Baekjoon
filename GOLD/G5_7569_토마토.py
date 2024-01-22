from collections import deque

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]  # 토마토 3차원 배열

days = 0

queue = deque()

# 처음 토마토들의 위치 좌표를 tuple형식으로 큐에 추가
for i in range(h):  # 층 수
    for j in range(n):  # 세로
        for k in range(m):  # 가로
            if tomato[i][j][k] == 1:
                queue.append((i, j, k, 0))

# bfs 진행
while queue:
    now_i, now_j, now_k, day = queue.popleft()
    days = max(days, day)
    for di, dj, dk in (0, 1, 0), (1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1):
        ni, nj, nk = now_i + di, now_j + dj, now_k + dk
        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m and not tomato[ni][nj][nk]:
            tomato[ni][nj][nk] = 1
            queue.append((ni, nj, nk, day + 1))

# bfs 종료 후에도 배열 내에 0이 존재한다면 -1로 출력
for i in range(h):
    for j in range(n):
        if 0 in tomato[i][j]:
            days = -1

print(days)