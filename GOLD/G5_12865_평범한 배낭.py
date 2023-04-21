import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    item.append([W, V])
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= item[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item[i][0]] + item[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])