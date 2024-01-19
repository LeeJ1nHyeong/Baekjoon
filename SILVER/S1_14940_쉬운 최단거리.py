from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]  # 방문표시 겸 목표까지의 거리, 벽이 아니지만 갈 수 없는 곳은 -1로 표시
queue = deque()  # bfs를 진행하기 위한 큐

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:  # 해당 위치가 목표지점이라면 bfs 시작
            visited[i][j] = 0  # 목표지점의 방문표시를 0으로 두고 시작
            queue.append((i, j))

            while queue:
                now_i, now_j = queue.popleft()
                # 4방향 델타 탐색
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = now_i + di, now_j + dj
                    # 다음 지역이 벽이 아니고 미방문 지역이라면 현재 위치의 visited값에 1을 더한 값을 저장 후 큐에 좌표 추가
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 1 and visited[ni][nj] == -1:
                        visited[ni][nj] = visited[now_i][now_j] + 1
                        queue.append((ni, nj))

        # 해당 위치가 벽이라면 visited에도 벽으로 표시
        elif board[i][j] == 0:
            visited[i][j] = 0

for v in visited:
    print(*v)