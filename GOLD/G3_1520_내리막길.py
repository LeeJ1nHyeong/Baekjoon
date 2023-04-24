import sys
input = sys.stdin.readline

def dfs(i, j):
    global dp
    if i == M - 1 and j == N - 1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < M and 0 <= nj < N and Map[ni][nj] < Map[i][j]:
            dp[i][j] += dfs(ni, nj)

    return dp[i][j]

M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

print(dfs(0, 0))