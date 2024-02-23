import sys
input = sys.stdin.readline

m, n = list(map(int, input().split()))
board = [1 for _ in range(2 * m - 1)]  # 제일 왼쪽 열, 제일 위쪽 행의 애벌레 성장을 저장하기 위한 1차원 리스트

# n일 동안 애벌레 성장
for _ in range(n):
    grow0, grow1, grow2 = map(int, input().split())

    for i in range(grow0, grow0 + grow1):
        board[i] += 1

    for i in range(grow0 + grow1, 2 * m - 1):
        board[i] += 2

# 성장 완료 후의 벌집 내 애벌레들을 2차원 리스트에 저장
ans = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        if j == 0:
            ans[i][j] = board[m - i - 1]
        else:
            ans[i][j] = board[m + j - 1]

for a in ans:
    print(*a)