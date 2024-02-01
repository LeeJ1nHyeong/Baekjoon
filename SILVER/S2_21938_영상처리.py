from collections import deque

n, m = map(int, input().split())
pixel = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

new_pixel = [[0] * m for _ in range(n)]  # RGB 평균값을 담을 리스트

for i in range(n):
    for j in range(m):
        # RGB 평균값이 경계값(t)보다 크거나 같다면 255를 저장
        average = sum(pixel[i][3 * j : 3 * j + 3]) // 3
        if average >= t:
            new_pixel[i][j] = 255

cnt = 0
queue = deque()
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        # bfs 진행
        if new_pixel[i][j] == 255 and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = 1

            # 첫 좌표 기준으로 255가 이어져있는 곳까지 bfs 진행
            while queue:
                now_i, now_j = queue.popleft()
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = now_i + di, now_j + dj
                    if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                        if new_pixel[ni][nj] == 255:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))

            cnt += 1  # bfs 종료 후 cnt 1 추가

print(cnt)