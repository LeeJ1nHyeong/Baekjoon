import sys
input = sys.stdin.readline

def backtrack(i, j, cnt):
    global max_cnt
    global visited

    if cnt > max_cnt:
        max_cnt = cnt

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C:
            idx = ord(board[ni][nj]) - 65
            if not alpha_list[idx]:
                alpha_list[idx] = True
                backtrack(ni, nj, cnt + 1)
                alpha_list[idx] = False

R, C = map(int, input().split())
board = [list(str(input())) for _ in range(R)]
alpha_list = [False] * 26
alpha_list[ord(board[0][0]) - 65] = True
max_cnt = 0

backtrack(0, 0, 1)

print(max_cnt)