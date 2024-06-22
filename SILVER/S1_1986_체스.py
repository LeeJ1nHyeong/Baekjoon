# 나이트 이동
def move_knight(i, j):
    global safe_area

    # 나이트가 이동할 수 있는 8방향 탐색
    for di, dj in (1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1):
        ni, nj = i + di, j + dj

        # 범위 밖으로 벗어나면 continue
        if ni < 0 or ni >= n or nj < 0 or nj >= m:
            continue

        # 다른 말이 있거나 방문 지역이라면 continue
        if board[ni][nj]:
            continue

        # 미방문 지역에는 방문 표시 후 안전 구역 1 차감
        if not board[ni][nj]:
            board[ni][nj] = 1
            safe_area -= 1

# 퀸 이동
def move_queen(i, j):
    global safe_area

    # 8방향으로 탐색 진행
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
        ni, nj = i + di, j + dj
        while True:
            # 범위 밖으로 벗어나거나 다른 말이 있다면 break
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                break

            if board[ni][nj] < 0:
                break

            # 미방문 지역에는 방문 표시 후 안전 구역 1 차감
            if not board[ni][nj]:
                board[ni][nj] = 1
                safe_area -= 1
            ni += di
            nj += dj


n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]

safe_area = n * m  # 안전 구역 수

# 퀸(-1), 나이트(-2), 폰(-3) 순서로 board에 배치
for num in range(1, 4):
    k, *lst = map(int, input().split())

    for i in range(k):
        r, c = lst[2 * i], lst[2 * i + 1]
        board[r - 1][c - 1] = -num
        safe_area -= 1

# 퀸, 나이트의 위치에 따른 안전 구역 탐색
for i in range(n):
    for j in range(m):
        if board[i][j] == -1:
            move_queen(i, j)
        elif board[i][j] == -2:
            move_knight(i, j)

# 안전 구역 수 출력
print(safe_area)
