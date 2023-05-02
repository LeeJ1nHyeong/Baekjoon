import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(str(input().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append([0, 0])
visited[0][0] = 1

while queue:
    i, j = queue.popleft()
    if i == N - 1 and j == M - 1:
        break
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == '1' and not visited[ni][nj]:
            visited[ni][nj] = visited[i][j] + 1
            queue.append([ni, nj])

print(visited[N - 1][M - 1])