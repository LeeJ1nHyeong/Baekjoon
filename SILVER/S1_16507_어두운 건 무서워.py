r, c, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

dp = [[0] * (c + 1) for _ in range(r + 1)]

# 누적 합 계산
for i in range(1, r + 1):
    for j in range(1, c + 1):
        dp[i][j] = board[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

# 두 좌표로 구성된 직사각형 내의 픽셀 밝기 합을 누적 합을 활용하여 계산
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    pixel_cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
    brightness = dp[r2][c2] - dp[r1 - 1][c2] - dp[r2][c1 - 1] + dp[r1 - 1][c1 - 1]
    avg = brightness // pixel_cnt

    print(avg)  # 밝기 평균 출력
