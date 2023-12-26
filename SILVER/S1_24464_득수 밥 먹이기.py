n = int(input())
dp = [1, 1, 1, 1, 1]  # 밥X, 1번, 2번, 3번, 4번

for _ in range(n - 1):
    temp = [0 for _ in range(5)]  # 이전 dp 값을 활용하기 위한 임시 리스트
    temp[0] = (dp[1] + dp[2] + dp[3] + dp[4]) % 1000000007
    temp[1] = (dp[0] + dp[3] + dp[4]) % 1000000007
    temp[2] = (dp[0] + dp[4]) % 1000000007
    temp[3] = (dp[0] + dp[1]) % 1000000007
    temp[4] = (dp[0] + dp[1] + dp[2]) % 1000000007
    dp = temp

print(sum(dp) % 1000000007)