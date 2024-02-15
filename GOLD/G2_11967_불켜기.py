from collections import deque

n, m = map(int, input().split())
switch = [[[] for _ in range(n)] for _ in range(n)]  # 해당 위치에서 불을 켤 수 있는 방의 스위치를 담을 3차원 배열
room = [[0] * n for _ in range(n)]  # 불이 켜졌는지를 확인하기 위한 2차원 배열
visited = [[0] * n for _ in range(n)]  # 방문 여부를 확인하기 위한 2차원 배열

# x - 1, y - 1 방에서 불을 켤 수 있는 좌표 a - 1, b - 1를 tuple형식으로 해당 좌표에 추가
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switch[x - 1][y - 1].append((a - 1, b - 1))

# bfs 초기 세팅
cnt = 1
queue = deque([(0, 0)])
room[0][0] = 1  # 처음 방은 불이 켜진 상태로 시작
visited[0][0] = 1  # 처음 방 방문 표시

# bfs 진행
while queue:
    i, j = queue.popleft()

    # 해당 위치에 스위치가 있을 경우 스위치를 켜기
    if switch[i][j]:
        for x, y in switch[i][j]:
            if not room[x][y]:
                cnt += 1
                room[x][y] = 1
                for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny]:  # 스위치를 켠 방이 방문표시가 되어있다면 queue에 추가
                            queue.append((nx, ny))

    # 스위치를 다 켜고 4방향 탐색하여 불이 켜진 곳 중 미방문지역 찾기
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            if not visited[ni][nj] and room[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj))

print(cnt)