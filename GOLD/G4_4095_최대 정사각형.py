while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    # 원활한 탐색을 위해 1행과 1열에 모두 0을 추가한 2차원 리스트 생성
    board = [[0 for _ in range(m + 1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 탐색 좌표가 0이면 continue
            if not board[i][j]:
                continue

            # 탐색 좌표가 1이면 현재 좌표의 위, 왼쪽, 왼쪽 위의 값 중 최솟값에 1을 더한 값을 dp에 저장
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # dp 내의 최댓값 출력
    ans = 0
    for d in dp:
        ans = max(ans, max(d))

    print(ans)
