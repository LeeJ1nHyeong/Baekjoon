# 오델로
def othello(r, c, color):
    global black, white

    board[r][c] = color  # 각 턴에 해당하는 돌을 두기
    change = []  # 뒤집을 돌의 좌표를 담을 리스트

    # 돌을 놓은 위치 기준 8방향 탐색 진행
    for d in range(8):
        nr, nc = r, c
        temp = []  # 방향별 뒤집을 돌의 좌표를 담을 리스트
        while True:
            nr, nc = nr + dr[d], nc + dc[d]
            # 게임판 범위를 벗어나면 바로 while문 종료
            if nr < 0 or nr == 6 or nc < 0 or nc == 6:
                break

            # 빈칸이라면 바로 while문 종료
            if board[nr][nc] == ".":
                break

            # 같은 색을 만날 경우
            if board[nr][nc] == color:
                change += temp  # temp에 모은 좌표들을 change에 추가
                # 이 후 뒤집은 돌의 개수를 해당하는 색에 추가 후 while문 종료
                if color == "B":
                    black += len(temp)
                else:
                    white += len(temp)
                break

            # 다른 색을 만날 경우, temp에 좌표 추가
            temp.append((nr, nc))

    # change에 모은 좌표들을 해당 색으로 뒤집기
    for i, j in change:
        board[i][j] = color


n = int(input())

# 초기 세팅
board = [["."] * 6 for _ in range(6)]
board[2][2] = board[3][3] = "W"
board[2][3] = board[3][2] = "B"

# 12시 방향부터 시계방향 순서
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

black, white = 2, 2  # 흑돌, 백돌 개수

# 흑돌부터 번갈아가면서 게임 진행
for i in range(n):
    r, c = map(int, input().split())
    if i % 2:
        white += 1
        othello(r - 1, c - 1, "W")
    else:
        black += 1
        othello(r - 1, c - 1, "B")

# 형식에 맞게 게임판 출력
for b in board:
    print("".join(b))

# 승자 출력
print("Black" if black > white else "White")
