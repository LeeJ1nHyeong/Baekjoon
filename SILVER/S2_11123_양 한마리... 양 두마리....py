from collections import deque

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0  # 양 무리 개수
    for i in range(h):
        for j in range(w):
            # 풀(".")이거나 방문 지역은 continue
            if board[i][j] == ".":
                continue

            if visited[i][j]:
                continue

            # bfs 초기 세팅
            queue = deque([(i, j)])
            visited[i][j] = 1

            # bfs 진행
            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj

                    if ni < 0 or ni == h or nj < 0 or nj == w:
                        continue

                    if board[ni][nj] == ".":
                        continue

                    if visited[ni][nj]:
                        continue

                    # 조건에 맞는 지역에 대해 방문 표시 후 queue에 추가
                    visited[ni][nj] = 1
                    queue.append((ni, nj))

            # bfs 종료 후 양 무리 개수 1 추가
            cnt += 1

    # 양 무리 개수 출력
    print(cnt)
