from collections import deque

def bfs():  # bfs
    queue = deque()
    visited = [[0] * c for _ in range(r)]  # 방문 표시 및 이동 횟수 저장을 위한 2차원 배열

    # 지훈이의 위치(J)를 먼저 queue에 담음
    for i in range(r):
        for j in range(c):
            if maze[i][j] == "J":
                visited[i][j] = 1  # 이동 횟수를 1로 저장
                queue.append((i, j))

    # J위치 저장 후 불의 위치(F)를 queue에 담음
    for i in range(r):
        for j in range(c):
            if maze[i][j] == "F":
                queue.append((i, j))

    # bfs 진행
    while queue:
        i, j = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            # 다음 위치가 미로를 탈출하는 것이고 현재 위치가 J라면 현재 좌표의 visited 값을 return하고 bfs 종료
            if ni < 0 or ni >= r or nj < 0 or nj >= c:
                if maze[i][j] == "J":
                    return visited[i][j]
            else:
                # 현재 위치가 불(F)이고 다음 위치가 벽이 아닐 경우
                if (maze[ni][nj] == "." or maze[ni][nj] == "J") and maze[i][j] == "F":
                    maze[ni][nj] = "F"  # 다음 위치를 F로 바꾸고
                    queue.append((ni, nj))  # 좌표를 queue에 저장
                # 현재 위치가 지훈(J)이고 다음 위치가 이동 가능할 경우
                elif maze[ni][nj] == "." and maze[i][j] == "J" and not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1  # 현재 visited에 1을 더한 값을 다음 visited에 저장하고
                    maze[ni][nj] = "J"  # 다음 위치를 J로 바꾼 후
                    queue.append((ni, nj))  # 좌표를 queue에 저장

    return "IMPOSSIBLE"  # while문이 종료됐다면 탈출 불가이므로 "IMPOSSIBLE" return

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]

print(bfs())