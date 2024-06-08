import sys
input = sys.stdin.readline


m, n = map(int, input().split())
k = int(input())
board = [list(input()) for _ in range(m)]
jungle = [[0] * (n + 1) for _ in range(m + 1)]  # 정글 누적 합
ocean = [[0] * (n + 1) for _ in range(m + 1)]  # 바다 누적 합
ice = [[0] * (n + 1) for _ in range(m + 1)]  # 얼음 누적 합

for i in range(1, m + 1):
    for j in range(1, n + 1):
        # 각 영역 별로 누적 합 저장
        jungle[i][j] = jungle[i - 1][j] + jungle[i][j - 1] - jungle[i - 1][j - 1]
        ocean[i][j] = ocean[i - 1][j] + ocean[i][j - 1] - ocean[i - 1][j - 1]
        ice[i][j] = ice[i - 1][j] + ice[i][j - 1] - ice[i - 1][j - 1]

        # 현재 좌표에 해당하는 영역에 1 추가
        if board[i - 1][j - 1] == "J":
            jungle[i][j] += 1
        elif board[i - 1][j - 1] == "O":
            ocean[i][j] += 1
        elif board[i - 1][j - 1] == "I":
            ice[i][j] += 1

# 직사각형 범위 내에 있는 정글, 바다, 얼음의 수를 누적 합을 이용하여 계산 후 출력
for _ in range(k):
    a, b, c, d = map(int, input().split())

    j_cnt = jungle[c][d] - jungle[a - 1][d] - jungle[c][b - 1] + jungle[a - 1][b - 1]
    o_cnt = ocean[c][d] - ocean[a - 1][d] - ocean[c][b - 1] + ocean[a - 1][b - 1]
    i_cnt = ice[c][d] - ice[a - 1][d] - ice[c][b - 1] + ice[a - 1][b - 1]

    print(j_cnt, o_cnt, i_cnt)
