t = int(input())

for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:  # n == 1일 경우의 예외처리
        print(max(stickers[0][0], stickers[1][0]))  # 두 값 중 최댓값 출력

    else:
        dp = [[0] * 2 for _ in range(n)]

        # dp 초기 설정
        dp[0] = [stickers[0][0], stickers[1][0]]
        dp[1] = [dp[0][1] + stickers[0][1], dp[0][0] + stickers[1][1]]  # 1번 인덱스와 대각선 방향의 이전 값을 더해서 저장

        # 현재 인덱스에서 2칸 이전의 dp 값들과 1칸 이전의 대각선 dp값 중 최댓값을 현재 스티커 위치의 값과 더해서 dp에 저장
        for i in range(2, n):
            dp[i][0] = stickers[0][i] + max(dp[i - 1][1], dp[i - 2][0], dp[i - 2][1])
            dp[i][1] = stickers[1][i] + max(dp[i - 1][0], dp[i - 2][0], dp[i - 2][1])

        print(max(dp[n - 1]))  # 마지막 인덱스의 두 값 중 최댓값 출력