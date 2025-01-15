n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

ans = 0

for k in range(0, min(n, m)):
    for i in range(n - k):
        for j in range(m - k):
            if board[i][j] == board[i + k][j] == board[i][j + k] == board[i + k][j + k]:
                ans = max(ans, (k + 1) ** 2)

print(ans)
