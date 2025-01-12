from collections import deque

# 백신 놓기 전과 놓은 후를 비교하여 다른 값이 있는지 확인
def vaccine():
    for i in range(n):
        for j in range(m):
            if before[i][j] == after[i][j]:
                continue

            bfs(i, j, after[i][j])

            return "YES" if check() else "NO"

    return "YES"


def bfs(i, j, change):
    visited = [[0] * m for _ in range(n)]
    target = before[i][j]
    queue = deque([(i, j)])
    visited[i][j] = 1

    while queue:
        ci, cj = queue.popleft()
        before[ci][cj] = change

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == n or nj < 0 or nj == m:
                continue

            if before[ni][nj] != target:
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

# 백신 여부 확인
def check():
    for i in range(n):
        for j in range(m):
            if before[i][j] != after[i][j]:
                return False

    return True


n, m = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]

print(vaccine())
