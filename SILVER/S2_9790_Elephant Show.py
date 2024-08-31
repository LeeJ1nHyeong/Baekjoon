from collections import deque

# 코끼리 위치 탐색
def search_elephant():
    for i in range(h):
        for j in range(w):
            # 코끼리의 좌표를 queue에 추가 후 방문 표시
            if board[i][j] == "A":
                queue.append((i, j))
                visited[i][j] = 1
                return


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    board = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 1  # 코끼리가 이동 가능한 타일 개수
    queue = deque()

    search_elephant()  # 코끼리 위치 탐색

    # bfs
    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == h or nj < 0 or nj == w:
                continue

            if board[ni][nj] == "#":
                continue

            if visited[ni][nj]:
                continue

            # 이동 가능한 조건을 모두 만족하면 방문 표시, queue에 좌표 추가, 타일 개수 1 추가
            visited[ni][nj] = 1
            cnt += 1
            queue.append((ni, nj))

    # 코끼리가 이동 가능한 타일 개수 출력
    print(cnt)
