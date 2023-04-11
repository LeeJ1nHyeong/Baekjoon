import sys
from collections import deque
import copy

def bfs():
    global max_safe
    lab2 = copy.deepcopy(lab)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if lab2[i][j] == 2:
                queue.append((i, j))

    while queue:
        si, sj = queue.popleft()
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and lab2[ni][nj] == 0:
                lab2[ni][nj] = 2
                queue.append((ni, nj))

    safe = 0

    for i in range(N):
        for j in range(M):
            if lab2[i][j] == 0:
                safe += 1

    if safe > max_safe:
        max_safe = safe

def backtrack(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    backtrack(cnt + 1)
                    lab[i][j] = 0


N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

max_safe = 0

backtrack(0)

print(max_safe)