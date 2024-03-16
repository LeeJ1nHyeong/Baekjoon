n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 각 좌표에서 놓여진 파이프의 방향 별 경우의 수를 표현하기 위한 3차원 리스트
# 0 : 가로, 1 : 대각선, 2 : 세로
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

# 처음에는 (1, 1), (1, 2)에 가로로 놓여있으므로 해당 위치의 가로 칸에 1 추가
dp[0][1][0] = 1

# 1행 처리
for i in range(2, n):
    if board[0][i] == 0:  # 다음 칸이 벽이 아니라면 이전 칸의 값을 저장
        dp[0][i][0] = dp[0][i - 1][0]

# dp 진행
for i in range(1, n):
    for j in range(1, n):
        # 대각선 파이프
        # 대각선 이동 경로에 벽이 없다면 (i - 1, j - 1) 칸의 모든 경우의 수를 현재 좌표의 대각선 칸에 더하여 저장
        if board[i][j] == 0 and board[i][j - 1] == 0 and board[i - 1][j] == 0:
            dp[i][j][1] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

        # 가로, 세로 파이프
        if board[i][j] == 0:  # 현재 좌표가 벽이 아니라면 각 모양에 알맞게 이전 값을 더하여 저장
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            dp[i][j][2] = dp[i - 1][j][2] + dp[i - 1][j][1]

print(sum(dp[n - 1][n - 1]))  # (n - 1, n - 1) 칸의 모든 경우의 수를 더하여 출력