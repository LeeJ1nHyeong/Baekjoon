# BFS를 이용한 풀이

from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]  # 부순 벽의 개수를 저장하기 위한 리스트
                                        # 원활한 진행을 위해 -1로 시작

# 초기 설정
visited[0][0] = 0

queue = deque()
queue.append((0, 0))

# bfs 진행
# 다음 방의 색깔에 따라 경우의 수를 나눠서 진행
while queue:
    i, j = queue.popleft()

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            # 다음 방이 흰 방일 경우
            if board[ni][nj] == "1":
                # 미방문 지역이라면 현재 방의 visited 값을 그대로 저장 후 queue에 좌표 추가
                if visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j]
                    queue.append((ni, nj))
                # 방문 지역이라면 현재 방의 visited 값과 다음 방의 visited 값 중 최솟값을 저장한 후 queue에 좌표 추가
                else:
                    if visited[ni][nj] > visited[i][j]:
                        visited[ni][nj] = visited[i][j]
                        queue.append((ni, nj))

            # 다음 방이 검은 방일 경우
            else:
                # 미방문 지역일 경우 현재 방의 visited 값에 1을 더한 값을 저장 후 queue에 좌표 추가
                if visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj))
                # 방문 지역이라면 현재 방의 visited 값과 다음 방의 visited 값에 1을 더한 값 중 최솟값을 저장한 후 queue에 좌표 추가
                else:
                    if visited[ni][nj] > visited[i][j] + 1:
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append((ni, nj))

print(visited[n - 1][n - 1])