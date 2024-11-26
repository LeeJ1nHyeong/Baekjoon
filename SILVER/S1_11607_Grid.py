'''
좌상단에서 우하단까지 최소 이동 거리 구하기

현재 위치에 적힌 숫자(k)만큼만 4방향으로 이동 가능 (정확하게 k칸만 이동 가능)

이동 불가 시 "IMPOSSIBLE" 출력
'''

from collections import deque


def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0] = 1

    while queue:
        ci, cj, move = queue.popleft()

        if (ci, cj) == (n - 1, m - 1):
            return move

        k = int(grid[ci][cj])
        if k == 0:
            continue

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di * k, cj + dj * k

            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))

    return "IMPOSSIBLE"


n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

print(bfs())
