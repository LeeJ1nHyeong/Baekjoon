import sys
input = sys.stdin.readline

def backtrack(i, j, cnt, ans):
    global max_ans

    if cnt == 4:
        max_ans = max(max_ans, ans)
        return

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            ans += paper[ni][nj]
            backtrack(ni, nj, cnt + 1, ans)
            visited[ni][nj] = False
            ans -= paper[ni][nj]

def h(i, j):
    global max_ans
    center = paper[i][j]
    EWSN = []

    if 0 <= i - 1 < N:
        EWSN.append(paper[i - 1][j])
    if 0 <= i + 1 < N:
        EWSN.append(paper[i + 1][j])
    if 0 <= j - 1 < M:
        EWSN.append(paper[i][j - 1])
    if 0 <= j + 1 < M:
        EWSN.append(paper[i][j + 1])

    if len(EWSN) >= 3:
        EWSN.sort(reverse=True)
        max_ans = max(max_ans, center + sum(EWSN[:3]))


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

max_ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        backtrack(i, j, 0, 0)
        visited[i][j] = False
        h(i, j)

print(max_ans)