n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

# dp에 누적 합 저장
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = num[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

k = int(input())

# 범위에 해당하는 합을 계산하여 출력
for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans = dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]
    print(ans)
    