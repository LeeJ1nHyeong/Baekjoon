import sys
input = sys.stdin.readline


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 누적 합 계산
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i - 1][j - 1]

k = int(input())

# 직사각형 범위 내의 사람 수를 누적 합을 이용하여 계산 후 출력
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    ans = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(ans)
