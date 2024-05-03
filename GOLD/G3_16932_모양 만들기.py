from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 방문 여부 체크용 2차원 리스트
area = [0]  # 각 영역별 넓이를 저장할 리스트

# 각 영역별 번호를 저장
num = 1  # 영역 번호
for i in range(n):
    for j in range(m):
        # 배열값이 1인 미방문 지역에 대해 bfs를 진행하여 영역 번호 지정
        if board[i][j] and not visited[i][j]:
            cnt = 1
            visited[i][j] = num
            queue = deque([(i, j)])

            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if board[ni][nj] and not visited[ni][nj]:
                            cnt += 1
                            visited[ni][nj] = num
                            queue.append((ni, nj))

            # bfs 종료 후 해당 영역의 넓이를 area에 추가 후 영역 번호 1 증가
            area.append(cnt)
            num += 1

max_cnt = 1  # 모양의 최대 넓이

# 배열값이 0인 곳을 탐색하여 해당 위치의 4방향의 영역 번호를 탐색하여 해당하는 넓이를 더하기
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt = 1
            area_visited = []  # 영역 번호 중복을 확인하기 위한 리스트
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj]:
                    area_num = visited[ni][nj]
                    # 해당 영역 번호가 중복이 아닐 경우 넓이를 더한 후 area_visited에 영역 번호 추가
                    if area_num not in area_visited:
                        area_visited.append(area_num)
                        cnt += area[area_num]

            # 모양의 최댓값 여부 확인
            max_cnt = max(max_cnt, cnt)

print(max_cnt)  # 최댓값 출력
