from collections import deque

r, c = map(int, input().split())
backyard = [list(input()) for _ in range(r)]
sheep, wolf = 0, 0  # 양, 늑대의 수

visited = [[0] * c for _ in range(r)]  # 방문 여부 체크용 2차원 리스트

for i in range(r):
    for j in range(c):
        # 벽이 아닌 미방문 지역를 시작으로 bfs 진행
        if backyard[i][j] != "#" and not visited[i][j]:
            # 초기 세팅
            queue = deque([(i, j)])
            visited[i][j] = 1
            # 해당 구역 내의 양, 늑대 수
            s, w = 0, 0
            # 첫 좌표가 양 또는 늑대일 경우 해당하는 변수에 1 증가
            if backyard[i][j] == "o":
                s += 1
            elif backyard[i][j] == "v":
                w += 1

            # bfs 진행
            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj
                    # 벽이 아닌 미방문 지역에 대해 양, 늑대일 경우 해당 변수 1 증가 후 좌표를 queue에 추가
                    if 0 <= ni < r and 0 <= nj < c and backyard[ni][nj] != "#" and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        if backyard[ni][nj] == "o":
                            s += 1
                        elif backyard[ni][nj] == "v":
                            w += 1
                        queue.append((ni, nj))

            # bfs 종료 후 양의 수가 더 많다면 양의 수를 더하고 같거나 늑대 수가 더 많다면 늑대 수를 더하기
            if s > w:
                sheep += s
            else:
                wolf += w

print(sheep, wolf)  # 양, 늑대의 수 출력