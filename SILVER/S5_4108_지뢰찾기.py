while True:
    r, c = map(int, input().split())
    if (r, c) == (0, 0):
        break

    board = [list(input()) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            # 빈칸 탐색
            if board[i][j] == ".":
                mine = 0  # 현재 위치 기준 주변 지뢰 개수

                # 현재 위치 기준으로 8방향에 지뢰가 있는지 탐색
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                    ni, nj = i + di, j + dj

                    # 범위 밖이라면 continue
                    if ni < 0 or ni == r or nj < 0 or nj == c:
                        continue

                    # 지뢰라면 mine 1 추가
                    if board[ni][nj] == "*":
                        mine += 1

                # 해당 위치에 지뢰 개수를 문자열로 저장
                board[i][j] = str(mine)

    # 형식에 맞게 출력
    for b in board:
        print("".join(b))
