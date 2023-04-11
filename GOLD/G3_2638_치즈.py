import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

hour = 0

while True:
    queue = deque()
    queue.append((0, 0))
    while queue:
        si, sj = queue.popleft()
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if grid[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = True
                elif grid[ni][nj] >= 1:
                    grid[ni][nj] += 1

    cheese_cnt = 0
    for i in range(N):
        for j in range(M):
            visited[i][j] = False
            if grid[i][j] >= 1:
                cheese_cnt += 1
                if grid[i][j] >= 3:
                    grid[i][j] = 0
                elif grid[i][j] == 2:
                    grid[i][j] = 1

    if cheese_cnt == 0:
        break
    hour += 1
    
print(hour)