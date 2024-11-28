'''
왼쪽 위에서 오른쪽 아래까지 이동 가능하면 "Yes", 이동 불가능하면 "No" 출력

이동은 오른쪽, 아래로만 가능

"x" : 장애물
'''

from collections import deque


def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        ci, cj = queue.popleft()

        if (ci, cj) == (n - 1, n - 1):
            return "Yes"

        for di, dj in (0, 1), (1, 0):
            ni, nj = ci + di, cj + dj

            if ni == n or nj == n:
                continue

            if board[ni][nj] == "x":
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

    return "No"


n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

print(bfs())
