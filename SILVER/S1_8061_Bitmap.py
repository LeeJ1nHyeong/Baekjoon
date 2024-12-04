'''
각 검은색 픽셀("0")에서 가장 가까이 있는 하얀색 픽셀("1")과의 거리를 출력
하얀색 픽셀일 경우에는 0으로 출력

'''

from collections import deque

n, m = map(int, input().split())
bitmap = [list(input()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if bitmap[i][j] == "1":
            visited[i][j] = 0
            queue.append((i, j))

while queue:
    ci, cj = queue.popleft()

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj

        if ni < 0 or ni == n or nj < 0 or nj == m:
            continue

        if bitmap[ni][nj] == "1":
            continue

        if visited[ni][nj] != -1:
            continue

        visited[ni][nj] = visited[ci][cj] + 1
        queue.append((ni, nj))

for v in visited:
    print(*v)
