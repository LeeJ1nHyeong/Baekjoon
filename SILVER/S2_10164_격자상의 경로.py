n, m, k = map(int, input().split())
dp = [[0] * m for _ in range(n)]

# 각 좌표별 이동경로 경우의 수를 dp 형태로 저장
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # 현재 좌표의 왼쪽값과 위쪽 값의 dp 합을 저장

# k가 0일 경우, 필수 방문 지역이 없다는 뜻이므로 dp 마지막 칸의 값을 출력
if k == 0:
    print(dp[n - 1][m - 1])

# k가 0이 아닐 경우
else:
    # k값에 해당하는 좌표를 구해서 저장
    ki, kj = 0, 0
    if k % m:
        ki, kj = k // m, k % m - 1
    else:
        ki, kj = k // m - 1, m - 1

    # ki, kj의 dp값과 이 좌표의 대칭 위치에 해당하는 좌표의 dp값을 곱해서 출력
    ans = dp[ki][kj] * dp[n - ki - 1][m - kj - 1]
    print(ans)
