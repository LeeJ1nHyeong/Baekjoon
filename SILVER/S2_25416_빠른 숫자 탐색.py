from collections import deque

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
visited = [[0] * 5 for _ in range(5)]

ans = -1  # 최소 이동 횟수, 도달 못하면 -1

# bfs 초기 세팅
queue = deque([(r, c, 0)])
visited[r][c] = 1

# bfs 진행
while queue:
    ci, cj, move = queue.popleft()

    # 현재 위치가 1이라면 ans를 이동 횟수로 최신화 후 bfs 종료
    if board[ci][cj] == 1:
        ans = move
        break

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj

        if ni < 0 or ni == 5 or nj < 0 or nj == 5:
            continue

        if board[ni][nj] == -1:
            continue

        if visited[ni][nj]:
            continue

        # 이동 조건에 만족하면 방문 표시 후 queue에 좌표 추가
        visited[ni][nj] = 1
        queue.append((ni, nj, move + 1))

# 최소 이동 횟수 출력
print(ans)
