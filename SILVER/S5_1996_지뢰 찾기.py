n = int(input())
board = [list(input()) for _ in range(n)]
mine_board = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 지뢰일 경우 mine_board에 "*"로 저장
        if board[i][j].isdigit():
            mine_board[i][j] = "*"

        # 빈칸일 경우
        else:
            cnt = 0  # 인접 칸 중 지뢰 개수

            # 현재 위치 기준 8방향 탐색
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                ni, nj = i + di, j + dj

                if ni < 0 or ni == n or nj < 0 or nj == n:
                    continue

                # 지뢰가 있다면 cnt에 지뢰 수 추가
                if board[ni][nj].isdigit():
                    cnt += int(board[ni][nj])

            # 9개를 넘길 경우 "M"으로 저장
            if cnt > 9:
                mine_board[i][j] = "M"
            else:
                mine_board[i][j] = cnt

# 형식에 맞게 출력
for i in range(n):
    for j in range(n):
        print(mine_board[i][j], end="")
    print()
