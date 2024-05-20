def check():
    for i in range(r):
        for j in range(c):
            if board[i][j] == ".":
                continue

            # 늑대 위치를 탐색
            if board[i][j] == "W":
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        # 늑대 근처 4방향에 양(S)이 붙어있다면 울타리(D)로 막을 수 없으므로 0 return
                        if board[ni][nj] == "S":
                            return 0
                        # 빈 칸(.)일 경우 울타리(D) 설치
                        if board[ni][nj] == ".":
                            board[ni][nj] = "D"

    return 1  # for문이 종료됐다면 울타리(D)로 막을 수 있다는 뜻이므로 1 return


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

# 문제 조건과 형식에 맞게 출력
if not check():
    print(0)
else:
    print(1)

    for b in board:
        print("".join(b))
