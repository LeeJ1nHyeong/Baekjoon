n = int(input())
dp = [0] * (n + 1)

if n == 1:  # n == 1일 때의 예외처리
    print(1)
else:
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):  # 이전 2개 값을 더한 값을 저장
        dp[i] = dp[i - 2] + dp[i - 1]

    print(dp[n] % 10007)  # 출력 형식에 맞게 작성