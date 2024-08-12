from collections import deque

n, m = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0  # 글자 개수
for i in range(n):
    for j in range(m):
        # 글씨가 아닐 경우 continue
        if not banner[i][j]:
            continue

        # 방문 지역일 경우 continue
        if visited[i][j]:
            continue

        # bfs 초기 세팅
        queue = deque([(i, j)])
        visited[i][j] = 1

        # bfs 진행
        while queue:
            ci, cj = queue.popleft()

            # 8방향 탐색
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == m:
                    continue

                if not banner[ni][nj]:
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                queue.append((ni, nj))

        # bfs 종료 후 글자 수 1 추가
        cnt += 1

# 글자 수 출력
print(cnt)
