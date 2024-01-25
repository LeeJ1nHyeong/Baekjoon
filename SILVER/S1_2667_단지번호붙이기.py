from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]  # 방문지역 표시용 리스트
houses = []  # 각 단지 별 집의 수를 담을 리스트

for i in range(n):
    for j in range(n):
        # 해당 지역에 집(1)이 있고 미방문 지역이라면 bfs 진행
        if board[i][j] == '1' and not visited[i][j]:

            # bfs 초기 설정
            visited[i][j] = 1
            cnt = 1

            queue = deque([(i, j)])

            # bfs 진행
            while queue:
                now_i, now_j = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = now_i + di, now_j + dj
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == '1' and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        cnt += 1
                        queue.append((ni, nj))

            houses.append(cnt)  # bfs 종료 후 집의 수를 리스트에 추가

print(len(houses))
houses.sort()  # 오름차순 정렬
for house in houses:
    print(house)