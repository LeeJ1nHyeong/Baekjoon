def is_heart(i, j):
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj

        if board[ni][nj] == "_":
            return False

    return True


n = int(input())
board = [list(input()) for _ in range(n)]
body = [0] * 5

heart_i, heart_j = 0, 0  # 심장 좌표

# 심장 좌표 찾기
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if board[i][j] == "_":
            continue

        if is_heart(i, j):
            heart_i, heart_j = i, j

# 왼쪽 팔
ci, cj = heart_i, heart_j
while True:
    cj -= 1
    if cj < 0 or board[ci][cj] == "_":
        break
    body[0] += 1

# 오른쪽 팔
ci, cj = heart_i, heart_j
while True:
    cj += 1
    if cj == n or board[ci][cj] == "_":
        break
    body[1] += 1

# 몸통
ci, cj = heart_i, heart_j
while True:
    ci += 1
    if board[ci][cj] == "_":
        break
    body[2] += 1

# 왼쪽 다리
ci, cj = heart_i + body[2] + 1, heart_j - 1
body[3] += 1
while True:
    ci += 1
    if ci == n or board[ci][cj] == "_":
        break
    body[3] += 1

# 오른쪽 다리
ci, cj = heart_i + body[2] + 1, heart_j + 1
body[4] += 1
while True:
    ci += 1
    if ci == n or board[ci][cj] == "_":
        break
    body[4] += 1

# 심장 위치와 팔, 다리, 허리 길이 출력
print(heart_i + 1, heart_j + 1)
print(*body)
