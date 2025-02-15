from collections import deque


def bfs(i, j):
    global top_list

    queue = deque([(i, j)])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1

    temp = []

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == n or nj < 0 or nj == m:
                continue

            if farm[ni][nj] > farm[ci][cj]:
                return False

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1

            if farm[ni][nj] == farm[ci][cj]:
                temp.append((ni, nj))
                queue.append((ni, nj))

    # while문이 종료된 후 꼭대기 좌표들을 추가하고 True return
    top_list += temp

    return True


n, m = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]

# 꼭대기 개수와 꼭대기 좌표
top = 0
top_list = []

for i in range(n):
    for j in range(m):
        if (i, j) in top_list:
            continue

        if bfs(i, j):
            top += 1

print(top)
