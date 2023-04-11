import sys
from collections import deque

def bfs(i, j, color):
    queue = deque()
    queue.append((i, j))
    while queue:
        si, sj = queue.popleft()
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == color and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = True


N = int(sys.stdin.readline())
grid = [list(str(sys.stdin.readline())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

normal_cnt = colorblind_cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j, grid[i][j])
            normal_cnt += 1

for i in range(N):
    for j in range(N):
        visited[i][j] = False
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j, grid[i][j])
            colorblind_cnt += 1

print(normal_cnt, colorblind_cnt)