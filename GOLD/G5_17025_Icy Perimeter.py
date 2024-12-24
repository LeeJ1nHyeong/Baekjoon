"""
아이스크림 덩어리 크기 중 최댓값과 그 덩어리의 둘레 출력
같은 크기의 덩어리가 여러 개 있을 경우, 둘레가 가장 작은 것으로 출력
"""

from collections import deque


def check(i, j):
    p = 0
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj

        if (ni < 0 or ni == n or nj < 0 or nj == n) or ((0 <= ni < n and 0 <= nj < n) and icecream[ni][nj] == "."):
            p += 1

    return p


n = int(input())
icecream = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

max_blob, max_blob_perimeter = 0, 0

for i in range(n):
    for j in range(n):
        if icecream[i][j] == "." or visited[i][j]:
            continue

        queue = deque([(i, j)])
        visited[i][j] = 1

        blob, perimeter = 0, 0
        while queue:
            ci, cj = queue.popleft()
            blob += 1
            perimeter += check(ci, cj)

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == n:
                    continue

                if icecream[ni][nj] == ".":
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                queue.append((ni, nj))

        if blob < max_blob:
            continue

        if blob == max_blob:
            max_blob_perimeter = min(perimeter, max_blob_perimeter)
            continue

        max_blob, max_blob_perimeter = blob, perimeter

print(max_blob, max_blob_perimeter)
