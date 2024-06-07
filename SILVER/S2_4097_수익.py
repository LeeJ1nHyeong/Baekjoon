import sys
input = sys.stdin.readline


while True:
    n = int(input())
    if n == 0:
        break

    # 수익을 리스트에 저장
    income = []
    for _ in range(n):
        income.append(int(input()))

    # dp 초기 설정
    dp = [0] * n
    dp[0] = income[0]

    # 이전 dp + 수익을 더한 값, 수익 둘 중 최댓값을 dp에 저장
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + income[i], income[i])

    print(max(dp))  # dp 최댓값 출력
