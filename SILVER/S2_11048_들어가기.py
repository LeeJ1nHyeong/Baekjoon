n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]  # dp

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 현재 위치 인덱스 기준 i - 1 위치와 j - 1 위치 중 최댓값과 현재의 maze 값을 더해서 dp에 저장
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + maze[i - 1][j - 1]

print(dp[n][m])