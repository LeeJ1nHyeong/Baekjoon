from collections import deque

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
i, j, k = map(int, input().split())

# bfs 초기 세팅
queue = deque([(i, j)])
visited[i][j] = 1
target = board[i][j]  # 바꿀 칸의 이전 번호
board[i][j] = k  # 시작 칸을 k로 변경

while queue:
    ci, cj = queue.popleft()

    # bfs 탐색을 진행하면서 target 값을 가진 인접 칸 탐색
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj

        if ni < 0 or ni == r or nj < 0 or nj == c:
            continue

        if board[ni][nj] != target:
            continue

        if visited[ni][nj]:
            continue

        visited[ni][nj] = 1
        board[ni][nj] = str(k)
        queue.append((ni, nj))

# 형식에 맞게 출력
for i in range(r):
    for j in range(c):
        print(board[i][j], end="")

    print()
