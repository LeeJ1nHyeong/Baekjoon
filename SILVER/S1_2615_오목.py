def backtrack(i, j, k, color, cnt):
    global winner
    global win_i, win_j

    if cnt == 5 and board[i + di[k]][j + dj[k]] != color:
        winner = color
        win_i, win_j = i, j

    else:
        ni, nj = i + di[k], j + dj[k]
        if 1 <= ni <= 19 and 1 <= nj <= 19 and board[ni][nj] == color:
            backtrack(ni, nj, k, color, cnt + 1)

board = [[0] * 21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0] * 21]

di = [-1, -1, 0, 1]   # 12시, 11시, 9시, 7시 순서
dj = [0, -1, -1, -1]

winner = 0
win_i, win_j = 0, 0

for i in range(1, 20):
    for j in range(1, 20):
        for k in range(4):
            if board[i][j] != 0 and 0 <= i - di[k] <= 21 and 0 <= j - dj[k] <= 21 and board[i][j] != board[i - di[k]][j - dj[k]]:
                color = board[i][j]
                backtrack(i, j, k, color, 1)

print(winner)
if winner:
    print(win_i, win_j)