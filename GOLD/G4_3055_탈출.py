from collections import deque

r, c = map(int, input().split())
forest = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

Di, Dj = 0, 0

ans = -1

queue = deque()

# 고슴도치 좌표를 먼저 큐에 추가, 굴의 위치는 따로 저장
for i in range(r):
    for j in range(c):
        if forest[i][j] == "S":
            queue.append((i, j))
        elif forest[i][j] == "D":
            Di, Dj = i, j

# 물의 위치 저장
for i in range(r):
    for j in range(c):
        if forest[i][j] == "*":
            queue.append((i, j))

# bfs 진행
while queue:
    now_i, now_j = queue.popleft()

    # 굴의 위치에 고슴도치가 도달했다면 이동 시간 저장 후 bfs 종료
    if forest[Di][Dj] == "S":
        ans = visited[Di][Dj]
        break

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = now_i + di, now_j + dj
        if 0 <= ni < r and 0 <= nj < c:
            # 해당 좌표가 물(*)이고 다음 이동 위치가 땅이거나 고슴도치 방문지역이라면 다음 이동 위치를 물로 바꾸고 큐에 좌표 추가
            if (forest[ni][nj] == "." or forest[ni][nj] == "S") and forest[now_i][now_j] == "*":
                forest[ni][nj] = "*"
                queue.append((ni, nj))
            # 해당 좌표가 고슴도치(S)이고 다음 이동 위치가 땅이거나 굴이라면 다음 이동 위치를 S로 바꾸고 현재 방문 지역에 1을 더한 값을 다음 이동 지역에 저장 후 큐에 좌표 추가
            elif (forest[ni][nj] == "." or forest[ni][nj] == "D") and forest[now_i][now_j] == "S":
                visited[ni][nj] = visited[now_i][now_j] + 1
                forest[ni][nj] = "S"
                queue.append((ni, nj))

# ans의 값에 따라 조건부 출력
if ans == -1:
    print("KAKTUS")
else:
    print(ans)