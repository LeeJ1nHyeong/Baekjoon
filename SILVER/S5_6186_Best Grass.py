# 풀("#")의 영역 개수 구하기

from collections import deque

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

cnt = 0  # 풀 영역 개수
for i in range(r):
    for j in range(c):
        # 탐색 위치가 "."이거나 방문했던 곳이라면 continue
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

            # 현재 위치 기준 상하좌우 4방향 탐색
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = ci + di, cj + dj

                # 범위 밖을 벗어나면 continue
                if ni < 0 or ni == r or nj < 0 or nj == c:
                    continue

                # "."이라면 continue
                if board[ni][nj] == ".":
                    continue

                # 방문한 곳이라면 continue
                if visited[ni][nj]:
                    continue

                # 방문 표시 후 queue에 좌표 추가
                visited[ni][nj] = 1
                queue.append((ni, nj))

        # while문 종료 후 cnt 1 추가
        cnt += 1

# 풀 영역 개수 출력
print(cnt)
