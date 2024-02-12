from collections import deque

n, m, k = map(int, input().split())
aisle = [[0] * m for _ in range(n)]  # 복도
visited = [[0] * m for _ in range(n)]  # 방문 여부

# 복도에 있는 음식물 쓰레기 표시
for _ in range(k):
    r, c = map(int, input().split())
    aisle[r - 1][c - 1] = 1

max_cnt = 0  # 뭉쳐있는 음식물 쓰레기의 최댓값

# 복도를 탐색하여 미방문한 음식물 쓰레기를 시작점으로 하여 bfs 진행
for i in range(n):
    for j in range(m):
        if aisle[i][j] and not visited[i][j]:
            queue = deque([(i, j)])
            cnt = 1
            visited[i][j] = 1

            while queue:
                now_i, now_j = queue.popleft()
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = now_i + di, now_j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if aisle[ni][nj] and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            cnt += 1
                            queue.append((ni, nj))

            max_cnt = max(cnt, max_cnt)  # 음식물 쓰레기 최댓값 여부 확인

print(max_cnt)