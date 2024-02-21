from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 방문 여부 체크용

cnt = 0  # 그림의 개수
max_area = 0  # 그림 넓이의 최댓값

# bfs
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            queue = deque([(i, j)])
            visited[i][j] = 1
            area = 1

            # bfs 진행
            while queue:
                now_i, now_j = queue.popleft()
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = now_i + di, now_j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if paper[ni][nj] == 1 and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            area += 1
                            queue.append((ni, nj))

            cnt += 1  # bfs 종료 후 그림 개수 1 추가
            max_area = max(area, max_area)  # 최대 넓이 여부 확인

print(cnt)
print(max_area)