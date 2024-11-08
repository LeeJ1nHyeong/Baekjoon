'''
검은색 픽셀("#")이 이어져 있는 구역의 개수 구하기
'''

from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

loop = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "." or visited[i][j]:
            continue

        queue = deque([(i, j)])
        visited[i][j] = 1

        while queue:
            ci, cj = queue.popleft()

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == m:
                    continue

                if board[ni][nj] == ".":
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                queue.append((ni, nj))

        loop += 1

print(loop)
