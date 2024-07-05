from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 방문 여부 체크용

ans = 0  # 나무 판자 개수
for i in range(n):
    for j in range(m):
        # 방문 지역은 탐색 제외
        if visited[i][j]:
            continue

        # 탐색 지역 좌표를 queue에 넣고 방문 표시
        queue = deque([(i, j)])
        visited[i][j] = 1

        # 가로 모양이면 가로 방향 탐색, 세로 모양이면 세로 방향 탐색
        if board[i][j] == "-":
            d = [(0, 1), (0, -1)]
        else:
            d = [(1, 0), (-1, 0)]

        # bfs 진행
        while queue:
            ci, cj = queue.popleft()

            for di, dj in d:
                ni, nj = ci + di, cj + dj

                # 범위 밖일 경우 continue
                if ni < 0 or ni == n or nj < 0 or nj == m:
                    continue

                # 방문 지역일 경우 continue
                if visited[ni][nj]:
                    continue

                # 다른 모양이라면 continue
                if board[ni][nj] != board[i][j]:
                    continue

                # 방문 표시 후 queue에 추가
                visited[ni][nj] = 1
                queue.append((ni, nj))

        # bfs 종료 후 ans 1 추가
        ans += 1

# 나무 판자 개수 출력
print(ans)
