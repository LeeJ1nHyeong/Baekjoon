'''
좌상단에서 우하단까지 오른쪽, 아래로만 갈 수 있는 경로의 수 출력

오른쪽, 아래로만 갈 수 있는 경로가 없을 경우
4방향으로 갈 수 있는 경로가 있다면 "THE GAME IS A LIE" 출력
4방향으로도 갈 수 있는 경로가 없다면 "INCONCEIVABLE" 출력

'''

from collections import deque


def bfs():
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    queue = deque([(1, 1)])
    visited[1][1] = 1

    while queue:
        ci, cj = queue.popleft()

        if (ci, cj) == (n, n):
            return "THE GAME IS A LIE"

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni <= 0 or ni > n or nj <= 0 or nj > n:
                continue

            if board[ni][nj] == "#":
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

    return "INCONCEIVABLE"


n = int(input())
board = [["." for _ in range(n + 1)]]

for _ in range(n):
    board.append(["."] + list(input()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][1] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == "#":
            continue

        if board[i - 1][j] == ".":
            dp[i][j] += dp[i - 1][j]

        if board[i][j - 1] == ".":
            dp[i][j] += dp[i][j - 1]

if dp[n][n]:
    print(dp[n][n] % (2 ** 31 - 1))
else:
    print(bfs())
