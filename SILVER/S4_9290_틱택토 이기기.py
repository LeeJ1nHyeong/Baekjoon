def tictactoe():
    for i in range(3):
        for j in range(3):
            # 빈칸인 곳을 탐색
            if board[i][j] != "-":
                continue

            # 빈칸에 말을 집어넣고 승리 여부 확인
            board[i][j] = piece
            # 한 줄을 완성 시켰다면 return
            if check():
                return
            
            # 완성이 되지 않았다면 빈칸으로 돌려놓기
            board[i][j] = "-"


def check():
    # 가로 및 세로 탐색
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == piece:
            return True
        if board[0][i] == board[1][i] == board[2][i] == piece:
            return True
        
    # 대각선 탐색
    if board[0][0] == board[1][1] == board[2][2] == piece:
        return True

    if board[0][2] == board[1][1] == board[2][0] == piece:
        return True

    return False  # 한 줄 완성이 되지 않았다면 False return


n = int(input())

for num in range(1, n + 1):
    board = [list(input()) for _ in range(3)]
    piece = input()

    tictactoe()  # 틱택토 진행

    # 형식에 맞게 출력
    print(f"Case {num}:")
    for b in board:
        print("".join(b))
