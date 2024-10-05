'''
호텔 내 방 넓이 중 최댓값 구하기
방이 없다면 -1 출력
'''

from collections import deque

n, m = map(int, input().split())
hotel = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

max_area = -1  # 방 넓이 최댓값

for i in range(n):
    for j in range(m):
        if hotel[i][j] == "*":
            continue
        if visited[i][j]:
            continue

        # bfs 초기 세팅
        queue = deque([(i, j)])
        visited[i][j] = 1
        area = 1

        # bfs 진행
        while queue:
            ci, cj = queue.popleft()

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == m:
                    continue

                if hotel[ni][nj] == "*":
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                area += 1
                queue.append((ni, nj))

        # 방 넓이 최댓값 여부 확인
        max_area = max(area, max_area)

print(max_area)
