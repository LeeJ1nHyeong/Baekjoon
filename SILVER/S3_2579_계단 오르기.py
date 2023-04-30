import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
    stair = int(input())
    stairs.append(stair)

stairs.append(0)

dp = [0] * (N + 2)

dp[1] = stairs[1]
dp[2] = dp[1] + stairs[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]

print(dp[N])