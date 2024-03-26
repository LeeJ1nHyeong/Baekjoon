n = int(input())

if n == 1:  # n == 1일 경우의 예외처리
    print(3)

else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 3

    # 규칙으로 생성된 점화식을 이용하여 dp에 값을 저장
    for i in range(2, n + 1):
        dp[i] = (3 * dp[i - 2] + 2 * (dp[i - 1] - dp[i - 2])) % 9901  # 조건에 맞게 9901로 나눈 나머지를 dp에 저장

    print(dp[n])
    