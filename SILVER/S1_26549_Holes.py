'''
박스에 생긴 구멍 개수(section)과 모든 구멍 넓이의 총 합(space) 출력
'''

from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    box = [list(input()) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    section, space = 0, 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == "#" or visited[i][j]:
                continue

            queue = deque([(i, j)])
            visited[i][j] = 1
            space += 1

            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj

                    if ni < 0 or ni == n or nj < 0 or nj == m:
                        continue

                    if box[ni][nj] == "#":
                        continue

                    if visited[ni][nj]:
                        continue

                    visited[ni][nj] = 1
                    space += 1
                    queue.append((ni, nj))

            section += 1

    if section == 1 and space == 1:
        print(f"{section} section, {space} space")
    elif section == 1:
        print(f"{section} section, {space} spaces")
    else:
        print(f"{section} sections, {space} spaces")
