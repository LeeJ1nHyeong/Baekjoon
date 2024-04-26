n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]  # dp

# 현재 좌표의 왼쪽과 위쪽 값 중 최댓값과 board의 값을 더한 값을 dp에 저장
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = board[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
