from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

ripen_tomato = deque()

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            ripen_tomato.append((i, j, 0))

max_day = 0

while ripen_tomato:
    i, j, day = ripen_tomato.popleft()
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N  and 0 <= nj < M and tomato[ni][nj] == 0:
            ripen_tomato.append((ni, nj, day + 1))
            tomato[ni][nj] = day + 1
            max_day = day + 1

for i in range(N):
    if 0 in tomato[i]:
        max_day = -1
        break

print(max_day)