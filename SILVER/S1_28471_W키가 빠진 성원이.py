from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = 0  # 목적지로 이동 가능한 시작 지점 개수

queue = deque()

# 목적지("F")를 찾아 방문 표시 후 queue에 추가
for i in range(n):
    for j in range(n):
        if board[i][j] == "F":
            queue.append((i, j))
            visited[i][j] = 1

while queue:
    ci, cj = queue.popleft()

    # 목적지에서 탐색을 시작하기 때문에 반대로 아래 이동을 제외한 7방향 탐색 진행
    for di, dj in (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
        ni, nj = ci + di, cj + dj

        if ni < 0 or ni == n or nj < 0 or nj == n:
            continue

        if board[ni][nj] == "#":
            continue

        if visited[ni][nj]:
            continue

        visited[ni][nj] = 1
        queue.append((ni, nj))
        ans += 1

print(ans)
