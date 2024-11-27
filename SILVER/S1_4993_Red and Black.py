'''
이동 가능한 검은색 타일(".") 개수 구하기

4방향 이동 가능

빨간색 타일("#")로는 이동 불가

"@" : 시작 지점(검은색 타일로 간주함)

'''

from collections import deque


def bfs():
    visited = [[0] * m for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == "@":
                visited[i][j] = 1
                queue.append((i, j))

    cnt = 1

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == n or nj < 0 or nj == m:
                continue

            if board[ni][nj] == "#":
                continue

            if visited[ni][nj]:
                continue

            cnt += 1
            visited[ni][nj] = 1
            queue.append((ni, nj))

    return cnt


while True:
    m, n = map(int, input().split())

    if (m, n) == (0, 0):
        break

    board = [list(input()) for _ in range(n)]

    print(bfs())
