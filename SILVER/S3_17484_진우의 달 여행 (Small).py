def dfs(i, j, pre_d, total):  # dfs
    global ans
    if i == n:  # 모든 행을 탐색했을 경우 최솟값 여부 체크 후 dfs 종료
        ans = min(ans, total)
        return

    total += board[i][j]  # 현재 위치값을 더해주기

    # 이전 방향과 중복이 되지 않도록 다음 dfs 진행
    # 가장 왼쪽 열일 경우
    if j == 0:
        if pre_d != 2:
            dfs(i + 1, j, 2, total)
        dfs(i + 1, j + 1, 3, total)

    # 가장 오른쪽 열일 경우
    elif j == m - 1:
        if pre_d != 2:
            dfs(i + 1, j, 2, total)
        dfs(i + 1, j - 1, 1, total)

    # 나머지
    else:
        if pre_d != 1:
            dfs(i + 1, j - 1, 1, total)
        if pre_d != 2:
            dfs(i + 1, j, 2, total)
        if pre_d != 3:
            dfs(i + 1, j + 1, 3, total)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 600  # 최솟값

for j in range(m):
    dfs(0, j, 0, 0)

print(ans)