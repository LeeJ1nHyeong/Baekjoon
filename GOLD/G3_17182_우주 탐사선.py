def backtrack(now, cnt, time):
    global min_time

    if cnt == n:
        min_time = min(time, min_time)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            backtrack(i, cnt + 1, time + board[now][i])
            visited[i] = 0


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
min_time = 1e8

# 플로이드-워셜 알고리즘을 활용하여 최단경로 확인
for m in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][m] + board[m][j])

# 백트래킹으로 모든 경로 탐색
visited[k] = 1
backtrack(k, 1, 0)

print(min_time)
