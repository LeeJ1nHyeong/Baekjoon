from collections import deque

n = int(input())
space = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

asteroid = 0  # 소행성 개수
for i in range(n):
    for j in range(n):
        # 소행성이 아니거나 방문 지역은 continue
        if space[i][j] == ".":
            continue
        if visited[i][j]:
            continue

        # bfs 초기 세팅
        queue = deque([(i, j)])
        visited[i][j] = 1

        # bfs 진행
        while queue:
            ci, cj = queue.popleft()

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == n:
                    continue

                if space[ni][nj] == ".":
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                queue.append((ni, nj))

        # bfs 종료 후 소행성 개수 1 추가
        asteroid += 1

# 소행성 개수 출력
print(asteroid)
