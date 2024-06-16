n = int(input())
mine_board = [list(input()) for _ in range(n)]  # 지뢰 정보
open_board = [list(input()) for _ in range(n)]  # 열린 칸 정보

for i in range(n):
    for j in range(n):
        # 지뢰가 저장되어 있으면 탐색 제외
        if open_board[i][j] == "*":
            continue

        # 열린 칸일 경우 조건 확인
        if open_board[i][j] == "x":
            # 열린 칸에 지뢰가 있다면 모든 지뢰를 open_board에 저장
            if mine_board[i][j] == "*":
                for k in range(n):
                    for l in range(n):
                        if mine_board[k][l] == "*":
                            open_board[k][l] = "*"

            # 빈칸일 경우 현재 위치 기준 8방향을 탐색하여 지뢰 개수를 open_board에 저장
            else:
                cnt = 0
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1):
                    ni, nj = i + di, j + dj

                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    if mine_board[ni][nj] == ".":
                        continue

                    cnt += 1

                open_board[i][j] = str(cnt)

# 출력
for ob in open_board:
    print("".join(ob))
