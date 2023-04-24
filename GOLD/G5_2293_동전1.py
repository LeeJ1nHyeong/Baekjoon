import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [1] + [0 for _ in range(K)]

for _ in range(N):
    coin = int(input())
    for i in range(coin, K + 1):
        dp[i] += dp[i - coin]

print(dp[K])