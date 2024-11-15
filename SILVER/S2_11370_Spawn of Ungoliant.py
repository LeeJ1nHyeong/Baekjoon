from collections import deque

while True:
    w, h = map(int, input().split())

    if (w, h) == (0, 0):
        break

    board = [list(input()) for _ in range(h)]

    queue = deque()

    for i in range(h):
        for j in range(w):
            if board[i][j] == "S":
                queue.append((i, j))

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == h or nj < 0 or nj == w:
                continue

            if board[ni][nj] != "T":
                continue

            board[ni][nj] = "S"
            queue.append((ni, nj))

    for b in board:
        print("".join(b))
