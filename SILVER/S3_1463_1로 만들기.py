n = int(input())
dp = [0] * (n + 1)

if n == 1:  # n이 1일 경우 예외처리(조건이 n >= 1인 정수)
    print(0)

else:
    dp[2] = 1

    for i in range(3, n + 1):
        if i % 2 == 0 and i % 3:  # 2의 배수인 경우
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
        elif i % 3 == 0 and i % 2:  # 3의 배수인 경우
            dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
        elif i % 2 == 0 and i % 3 == 0:  # 2의 배수, 3의 배수 둘 다 해당될 경우
            dp[i] = min(dp[i // 2] + 1, dp[i // 3] + 1, dp[i - 1] + 1)
        else:  # 위 조건들에 해당되지 않는 나머지
            dp[i] = dp[i - 1] + 1

    print(dp[n])