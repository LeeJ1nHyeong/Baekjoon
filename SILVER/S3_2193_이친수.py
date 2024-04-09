# 전형적인 피보나치 수열

n = int(input())
dp = [0] * (n + 1)

dp[1] = 1  # n == 1일 때의 dp값은 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])