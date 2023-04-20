import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(str(input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

visited[0][0][0] = 1

queue = deque()
queue.append((0, 0, 0))

ans = -1

while queue:
    i, j, broken = queue.popleft()
    if i == N - 1 and j == M - 1:
        ans = visited[i][j][broken]
        break

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] == '1' and broken == 0:
                visited[ni][nj][1] = visited[i][j][0] + 1
                queue.append((ni, nj, 1))
            elif arr[ni][nj] == '0' and not visited[ni][nj][broken]:
                visited[ni][nj][broken] = visited[i][j][broken] + 1
                queue.append((ni, nj, broken))

print(ans)