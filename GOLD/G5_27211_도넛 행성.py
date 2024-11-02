from collections import deque

n, m = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

area = 0  # 탐험 가능한 구역 개수
for i in range(n):
    for j in range(m):
        if planet[i][j] or visited[i][j]:
            continue

        # bfs 초기 세팅
        queue = deque([(i, j)])
        visited[i][j] = 1

        while queue:
            ci, cj = queue.popleft()

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                # 위아래, 좌우 양 끝이 연결되어 있는 것을 주의
                ni, nj = (ci + di) % n, (cj + dj) % m

                if ni < 0 or ni == n or nj < 0 or nj == m:
                    continue

                if planet[ni][nj]:
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                queue.append((ni, nj))

        area += 1

print(area)
