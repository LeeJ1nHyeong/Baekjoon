import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = num_list[0]

for i in range(1, N):
    dp[i] = max(num_list[i], dp[i - 1] + num_list[i])

print(max(dp))