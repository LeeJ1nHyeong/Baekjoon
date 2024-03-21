def two_dots():
    global is_cycle

    for i in range(n):
        for j in range(m):
            # 미방문 지역을 찾아 방문 표시 후 dfs 진행
            if not visited[i][j]:
                visited[i][j] = 1
                dfs(board[i][j], i, j, 1, i, j)

                # dfs 후 사이클이 존재한다면 "Yes" return
                if is_cycle:
                    return "Yes"

    return "No"  # for문이 종료된다면 사이클이 없다는 뜻이므로 "No" return


def dfs(target, si, sj, cnt, i, j):
    global is_cycle

    if is_cycle:  # 사이클이 존재한다면 dfs 종료
        return

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            # 방문 개수가 4개 이상이고 시작지점으로 돌아왔다면 사이클이 존재하므로 True로 변환 후 종료
            if cnt >= 4 and ni == si and nj == sj:
                is_cycle = True
                return
            
            # 다음 좌표가 같은 색깔인 미방문 지역이라면 dfs 계속 진행
            if board[ni][nj] == target and not visited[ni][nj]:
                visited[ni][nj] = 1
                dfs(target, si, sj, cnt + 1, ni, nj)
                visited[ni][nj] = 0


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 방문 표시용 2차원 리스트
is_cycle = False  # 사이클 존재 여부

print(two_dots())
