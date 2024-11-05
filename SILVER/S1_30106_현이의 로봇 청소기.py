from collections import deque

n, m, k = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

ans = 0  # 청소기 작동 최소 횟수

for i in range(n):
    for j in range(m):
        # 미방문 지역을 시작점으로 하여 인접영역 탐색
        if visited[i][j]:
            continue

        # bfs 초기 세팅
        queue = deque([(i, j)])
        visited[i][j] = 1

        while queue:
            ci, cj = queue.popleft()

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == m:
                    continue

                # 두 지역의 높낮이 차이가 k를 초과하면 continue
                if abs(room[ci][cj] - room[ni][nj]) > k:
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                queue.append((ni, nj))

        ans += 1

print(ans)
