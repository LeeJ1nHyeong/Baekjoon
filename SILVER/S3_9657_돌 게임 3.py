n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1

for i in range(5, n + 1):
    if dp[i - 1] == 1 and dp[i - 3] == 1 and dp[i - 4] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

print("SK" if dp[n] else "CY")
