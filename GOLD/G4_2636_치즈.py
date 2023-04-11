import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1 ,0]

remain_cheese = []
cheese_cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheese_cnt += 1

remain_cheese.append(cheese_cnt)

while True:
    cheese_cnt = 0
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if board[ni][nj] == 0 and not visited[ni][nj]:
                    queue.append((ni, nj))
                elif board[ni][nj] == 1:
                    board[ni][nj] = 0
                visited[ni][nj] = True

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cheese_cnt += 1
    remain_cheese.append(cheese_cnt)

    if cheese_cnt == 0:
        break

    for y in range(N):
        for x in range(M):
            visited[y][x] = False

print(len(remain_cheese) - 1)
print(remain_cheese[-2])