from collections import deque


def bfs():
    queue = deque()

    # 딱따구리 식구(2)의 좌표에 대해 방문 표시 후 queue에 저장
    for i in range(n):
        for j in range(m):
            if board[i][j] == "2":
                visited[i][j] = 1
                queue.append((i, j, 0))

    # bfs 진행
    while queue:
        ci, cj, move = queue.popleft()

        # 음식 중 하나에 도달했다면 "TAK" 출력 후 이동 횟수 return
        if board[ci][cj] in ("3", "4", "5"):
            print("TAK")
            return move

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == n or nj < 0 or nj == m:
                continue

            if board[ni][nj] == "1":
                continue

            if visited[ni][nj]:
                continue

            # 이동 가능한 위치에 대해 방문 표시 후 queue에 좌표 추가
            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))

    return "NIE"  # while문이 종료됐다면 음식에 도달을 못한다는 뜻이므로 "NIE" return


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

print(bfs())
