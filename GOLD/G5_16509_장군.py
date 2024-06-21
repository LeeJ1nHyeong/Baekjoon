from collections import deque

# bfs
def bfs():
    # bfs 초기 세팅
    visited[r1][c1] = 1
    queue.append((r1, c1, 0))  # 상의 좌표, 이동 횟수를 튜플 형태로 queue에 추가

    # bfs 진행
    while queue:
        ci, cj, move = queue.popleft()

        # 왕의 위치라면 이동 횟수 return
        if (ci, cj) == (r2, c2):
            return move
        
        # 4방향 직선 한 칸 이동한 위치 탐색
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            # 범위 밖으로 벗어나거나 왕이 길을 막고 있다면 continue
            if ni < 0 or ni >= 10 or nj < 0 or nj >= 9:
                continue

            if (ni, nj) == (r2, c2):
                continue

            # 각 4방향에서 대각선으로 이동한 위치 탐색
            if (di, dj) == (0, 1):
                cross_move(ni, nj, [(-1, 1), (1, 1)], move)

            elif (di, dj) == (1, 0):
                cross_move(ni, nj, [(1, -1), (1, 1)], move)

            elif (di, dj) == (0, -1):
                cross_move(ni, nj, [(-1, -1), (1, -1)], move)

            elif (di, dj) == (-1, 0):
                cross_move(ni, nj, [(-1, -1), (-1, 1)], move)

    return -1  # while문이 종료됐다면 이동 불가라는 뜻이므로 -1 return


# 대각선 이동
def cross_move(i, j, d_list, move):
    global queue

    for di, dj in d_list:
        ni, nj = i + di, j + dj

        # 범위 밖을 벗어나거나 왕이 길을 막고 있다면 continue
        if ni < 0 or ni >= 10 or nj < 0 or nj >= 9:
            continue

        if (ni, nj) == (r2, c2):
            continue

        # 대각선으로 한 칸씩 더 이동한 후 조건 확인
        ni += di
        nj += dj

        # 범위 밖을 벗어나거나 방문 지역이라면 continue
        if ni < 0 or ni >= 10 or nj < 0 or nj >= 9:
            continue

        if visited[ni][nj]:
            continue

        # 방문 표시 후 queue에 추가
        visited[ni][nj] = 1
        queue.append((ni, nj, move + 1))


r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
queue = deque()
visited = [[0] * 9 for _ in range(10)]  # 방문 표시 확인용

# bfs를 진행하여 나온 최소 이동 횟수 출력
print(bfs())