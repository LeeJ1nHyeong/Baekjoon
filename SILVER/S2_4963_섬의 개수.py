from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:  # 해당 지역이 땅(1)이고 미방문 지역이라면 bfs 진행

                # bfs 초기 설정
                queue = deque()
                queue.append((i, j))
                visited[i][j] = 1

                # bfs 진행
                while queue:
                    now_i, now_j = queue.popleft()

                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1):  # 대각선 포함 8방향 탐색
                        ni, nj = now_i + di, now_j + dj
                        if 0 <= ni < h and 0 <= nj < w and board[ni][nj] == 1 and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))

                cnt += 1  # bfs가 끝나면 방문 지역 전체가 하나의 섬이므로 cnt 1 추가

    print(cnt)