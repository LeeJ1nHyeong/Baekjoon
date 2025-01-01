def check(i, j):
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj

        if ni < 0 or ni == n or nj < 0 or nj == m:
            continue

        if visited[ni][nj]:
            return False

    return True


def backtrack(cnt, total, ci, cj):
    global ans

    if cnt == k:
        ans = max(ans, total)
        return

    for i in range(ci, n):
        for j in range(cj if i == ci else 0, m):
            if visited[i][j]:
                continue

            if check(i, j):
                visited[i][j] = 1
                backtrack(cnt + 1, total + board[i][j], i, j)
                visited[i][j] = 0


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ans = -1e9

backtrack(0, 0, 0, 0)

print(ans)
