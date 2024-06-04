from collections import deque


h, w = map(int, input().split())
sand_castle = [list(input()) for _ in range(h)]
visited = [[0] * w for _ in range(h)]  # 파도 횟수를 저장하기 위한 2차원 리스트

queue = deque()
for i in range(h):
    for j in range(w):
        # 모래성 내에 모래가 없는 부분은 0으로 치환 후 queue에 좌표 추가
        if sand_castle[i][j] == ".":
            sand_castle[i][j] = 0
            queue.append((i, j))

        # 모래가 있는 부분은 int형으로 치환
        else:
            sand_castle[i][j] = int(sand_castle[i][j])

wave = 0  # 파도 횟수

# bfs 진행
while queue:
    i, j = queue.popleft()

    # 현재 좌표 기준 8방향 탐색
    for di, dj in (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1):
        ni, nj = i + di, j + dj
        if ni < 0 or ni == h or nj < 0 or nj == w:
            continue

        # 모래가 있는 부분 탐색
        if sand_castle[ni][nj]:
            sand_castle[ni][nj] -= 1  # 모래 강도 1 감소
            # 감소 후 모래 강도가 0이라면 현재 좌표의 파도 횟수에 1을 더한 값을 저장
            if not sand_castle[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                wave = max(wave, visited[ni][nj])  # 파도 횟수 최신화
                queue.append((ni, nj))  # queue에 다음 좌표 추가

print(wave)  # 파도 횟수 출력
