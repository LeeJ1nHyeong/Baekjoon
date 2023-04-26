import sys
input = sys.stdin.readline

string1 = input().strip()
string2 = input().strip()
N, M = len(string1), len(string2)
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1] , dp[i - 1][j])

print(dp[N][M])