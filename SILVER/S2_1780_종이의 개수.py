def divide_and_conquer(x, y, n):
    target = board[x][y]  # 탐색할 번호
    divide = n // 3

    # 탐색 영역 내에 target과 다른 숫자가 있을 경우 9분할로 재탐색
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != target:
                # 9분할 윗줄
                divide_and_conquer(x, y, divide)
                divide_and_conquer(x, y + divide, divide)
                divide_and_conquer(x, y + 2 * divide, divide)

                # 9분할 중간줄
                divide_and_conquer(x + divide, y, divide)
                divide_and_conquer(x + divide, y + divide, divide)
                divide_and_conquer(x + divide, y + 2 * divide, divide)

                # 9분할 아랫줄
                divide_and_conquer(x + 2 * divide, y, divide)
                divide_and_conquer(x + 2 * divide, y + divide, divide)
                divide_and_conquer(x + 2 * divide, y + 2 * divide, divide)

                return
            
    # 탐색 영역 내 모든 숫자가 같을 경우 그 숫자에 해당하는 칸에 1 추가
    if target == -1:
        paper_cnt[0] += 1
    elif target == 0:
        paper_cnt[1] += 1
    else:
        paper_cnt[2] += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

paper_cnt = [0] * 3  # -1, 0, 1의 개수

divide_and_conquer(0, 0, n)  # 분할정복 진행

# -1, 0, 1의 개수를 순서대로 출력
for p in paper_cnt:
    print(p)
