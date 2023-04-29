import sys
input = sys.stdin.readline

N = int(input())
color_costs = list(list(map(int, input().split())) for _ in range(N))

dp = [[0] * 3 for _ in range(2)]

inf = 1000 * 1000 * 10

ans = inf

for k in range(3):
    dp[0][0], dp[0][1], dp[0][2] = inf, inf, inf
    dp[0][k] = color_costs[0][k]

    for i in range(1, N):
        dp[1][0] = min(dp[0][1], dp[0][2]) + color_costs[i][0]
        dp[1][1] = min(dp[0][0], dp[0][2]) + color_costs[i][1]
        dp[1][2] = min(dp[0][0], dp[0][1]) + color_costs[i][2]

        dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]

    ans = min(ans, min(dp[0][(k + 1) % 3], dp[0][(k + 2) % 3]))

print(ans)