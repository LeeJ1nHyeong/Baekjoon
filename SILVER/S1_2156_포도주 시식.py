import sys
input = sys.stdin.readline

N = int(input())
wines = [0]
for _ in range(N):
    wine = int(input())
    wines.append(wine)

wines.append(0)

dp = [0] * (N + 2)
dp[1] = wines[1]
dp[2] = dp[1] + wines[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i - 3]+wines[i - 1]+wines[i], dp[i - 2]+wines[i], dp[i - 1])

print(dp[N])