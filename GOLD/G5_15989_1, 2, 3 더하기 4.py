t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n + 1)  # DP 풀이용 리스트
    # n이 1, 2, 3일 경우에 대한 예외처리
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(3)

    # n이 4 이상일 경우
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        # 이전 인덱스 값과 (i-2번째 값과 i-3번째 값의 차이)값을 더해서 저장
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + (dp[i - 2] - dp[i - 3])
            if i % 3 == 0:  # 3의 배수일 경우 1 추가
                dp[i] += 1

        print(dp[n])