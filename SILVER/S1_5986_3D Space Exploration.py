from collections import deque

n = int(input())
space = [[list(input()) for _ in range(n)] for _ in range(n)]
visited = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if space[i][j][k] == "." or visited[i][j][k]:
                continue

            queue = deque([(i, j, k)])
            visited[i][j][k] = 1

            while queue:
                ci, cj, ck = queue.popleft()

                # 상하좌우, 앞뒤 총 6방향 탐색
                for di, dj, dk in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
                    ni, nj, nk = ci + di, cj + dj, ck + dk

                    if ni < 0 or ni == n or nj < 0 or nj == n or nk < 0 or nk == n:
                        continue

                    if space[ni][nj][nk] == ".":
                        continue

                    if visited[ni][nj][nk]:
                        continue

                    visited[ni][nj][nk] = 1
                    queue.append((ni, nj, nk))

            ans += 1

print(ans)
