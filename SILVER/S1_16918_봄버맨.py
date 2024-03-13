r, c, n = map(int, input().split())
board = [list(input()) for _ in range(r)]
bomb_time = [[-1] * c for _ in range(r)]  # 폭탄 설치 시간을 표시할 2차원 리스트

# 처음(1초)에 설치한 폭탄(O)를 찾고 폭탄 설치 시간 표시
for i in range(r):
    for j in range(c):
        if board[i][j] == "O":
            bomb_time[i][j] = 0

second = 1  # 폭탄 설치 시간
# n초까지 봄버맨 행동 진행
while second != n:
    second += 1

    # 폭탄 설치
    for i in range(r):
        for j in range(c):
            if board[i][j] == ".":
                board[i][j] = "O"
                bomb_time[i][j] = second

    # 폭탄 설치 후 3초가 지나면 해당 위치와 인접한 4칸이 폭발
    for i in range(r):
        for j in range(c):
            if bomb_time[i][j] == second - 3:
                board[i][j] = "."
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        board[ni][nj] = "."

# n초 후 맵 상태 출력
for b in board:
    print("".join(b))
