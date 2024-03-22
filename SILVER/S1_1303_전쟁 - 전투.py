from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]  # 방문 표시용 2차원 리스트
white, blue = 0, 0  # 아군 병사, 적군 병사

for i in range(m):
    for j in range(n):
        # 미방문 지역을 찾아 bfs 시작
        if not visited[i][j]:
            # bfs 초기 세팅
            visited[i][j] = 1
            queue = deque([(i, j)])
            target = board[i][j]

            cnt = 1  # 뭉쳐있는 병사 수
            # bfs 진행
            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        # 다음 좌표가 같은 병사인 미방문 지역에 대해 cnt 1 추가 및 해당 좌표 queue 추가
                        if board[ni][nj] == target and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            cnt += 1
                            queue.append((ni, nj))

            # 아군, 적군 여부에 따라 각 병사 수를 제곱해서 더하기
            if target == "W":
                white += cnt ** 2
            else:
                blue += cnt ** 2

print(white, blue)
