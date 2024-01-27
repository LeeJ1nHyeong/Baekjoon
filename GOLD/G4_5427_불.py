from collections import deque

def bfs():  # bfs
    while queue:
        i, j = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            # 다음 위치가 탈출이고 현재 위치에 @가 있다면 bfs 종료 및 현재 위치의 visited값 return
            if (ni < 0 or ni >= h or nj < 0 or nj >= w) and building[i][j] == "@":
                return visited[i][j]
            elif 0 <= ni < h and 0 <= nj < w:
                # 다음 위치가 불(*) 또는 벽(#)이 아니고 현재 위치가 불이라면 다음 위치를 불로 바꾸고 큐에 좌표 추가
                if (building[ni][nj] == "." or building[ni][nj] == "@") and building[i][j] == "*":
                    building[ni][nj] = "*"
                    queue.append((ni, nj))
                # 다음 위치가 빈 공간(.)이고 현재 위치가 @라면 현재 위치의 visited 값에 1을 더한 값을 다음 위치 visited에 저장하고
                # 다음 위치를 @로 바꾼 후 큐에 좌표 추가
                elif building[ni][nj] == "." and building[i][j] == "@":
                    visited[ni][nj] = visited[i][j] + 1
                    building[ni][nj] = "@"
                    queue.append((ni, nj))

    return "IMPOSSIBLE"  # 큐에 아무것도 없으면 탈출을 못했다는 뜻이므로 "IMPOSSIBLE" 문자열 return

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]  # 방문 표시용

    queue = deque()

    # 시작 위치를 먼저 찾아서 큐에 좌표 추가
    for i in range(h):
        for j in range(w):
            if building[i][j] == "@":
                visited[i][j] = 1  # 시작 좌표에 방문 표시
                queue.append((i, j))

    # 이후 불 위치 좌표를 큐에 추가
    for i in range(h):
        for j in range(w):
            if building[i][j] == "*":
                queue.append((i, j))

    print(bfs())  # bfs 진행