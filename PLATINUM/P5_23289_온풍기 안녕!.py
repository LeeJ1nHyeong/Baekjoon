from collections import deque


def check():
    for check_i, check_j in check_list:
        if temperature[check_i][check_j] < k:
            return False

    return True


r, c, k = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]  # 방
temperature = [[0] * c for _ in range(r)]  # 각 위치별 온도

# 우좌상하 순서로 벽 여부 저장
wall = [[[0, 0, 0, 0] for _ in range(c)] for _ in range(r)]

heater = []  # 온풍기 위치와 방향을 저장할 리스트
check_list = []  # 온도 조사 칸을 저장할 리스트

# 온풍기 및 온도 조사 칸 탐색
for i in range(r):
    for j in range(c):
        # 온풍기일 경우 heater에 위치와 방향을 튜플 형태로 저장
        if 1 <= room[i][j] <= 4:
            heater.append((i, j, room[i][j]))

        # 온도 조사 칸일 경우 check_list에 위치를 튜플 형태로 저장
        elif room[i][j] == 5:
            check_list.append((i, j))

# 벽 저장
w = int(input())
for _ in range(w):
    x, y, t = map(int, input().split())

    # 가로 벽일 경우 현재 좌표의 2번, 위 좌표의 3번 벽 표시
    if t == 0:
        wall[x - 1][y - 1][2] = 1
        wall[x - 2][y - 1][3] = 1

    # 세로 벽일 경우 현재 좌표의 0번, 오른쪽 좌표의 1번 벽 표시
    else:
        wall[x - 1][y - 1][0] = 1
        wall[x - 1][y][1] = 1

chocolate = 0  # 초콜릿 개수

# 최대 101번의 테스트 진행
for _ in range(101):
    # 온풍기 가동
    for i, j, d in heater:
        visited = [[0] * c for _ in range(r)]
        queue = deque()

        ## 각 방향별로 온풍기 작동 진행
        # 오른쪽 방향
        if d == 1:
            # 온풍기의 오른쪽 칸 방문 표시 후 온도 5 증가
            visited[i][j + 1] = 1
            temperature[i][j + 1] += 5

            # 위치, 증가할 온도를 튜플 형태로 queue에 저장
            queue.append((i, j + 1, 5))

            # bfs 진행
            while queue:
                ci, cj, t_up = queue.popleft()

                # 증가할 온도가 없다면 continue
                if not t_up:
                    continue

                # 위 대각선, 오른쪽, 아래 대각선 순서
                for di, dj in (-1, 1), (0, 1), (1, 1):
                    ni, nj = ci + di, cj + dj

                    # 범위를 벗어나거나 방문 지역은 continue
                    if ni < 0 or ni == r or nj < 0 or nj == c:
                        continue
                    if visited[ni][nj]:
                        continue

                    # 오른쪽 방향 진행 지역에 벽이 있다면 continue
                    if (di, dj) == (0, 1):
                        if wall[ci][cj][0]:
                            continue
                    # 각 대각선 방향 진행 지역에 벽이 있다면 continue
                    elif (di, dj) == (-1, 1):
                        if wall[ci][cj][2] or wall[ni][nj][1]:
                            continue
                    elif (di, dj) == (1, 1):
                        if wall[ci][cj][3] or wall[ni][nj][1]:
                            continue

                    # 방문 표시 및 온도 증가 후 queue에 추가
                    visited[ni][nj] = 1
                    temperature[ni][nj] += t_up - 1
                    queue.append((ni, nj, t_up - 1))

        ## 나머지 방향도 오른쪽 방향(d == 1)과 동일한 방식으로 알맞은 방향에 적용
        # 왼쪽 방향
        elif d == 2:
            visited[i][j - 1] = 1
            temperature[i][j - 1] += 5

            queue.append((i, j - 1, 5))

            while queue:
                ci, cj, t_up = queue.popleft()

                if not t_up:
                    continue

                for di, dj in (-1, -1), (0, -1), (1, -1):
                    ni, nj = ci + di, cj + dj

                    if ni < 0 or ni == r or nj < 0 or nj == c:
                        continue

                    if visited[ni][nj]:
                        continue

                    if (di, dj) == (0, -1):
                        if wall[ci][cj][1]:
                            continue

                    elif (di, dj) == (-1, -1):
                        if wall[ci][cj][2] or wall[ni][nj][0]:
                            continue

                    elif (di, dj) == (1, -1):
                        if wall[ci][cj][3] or wall[ni][nj][0]:
                            continue

                    visited[ni][nj] = 1
                    temperature[ni][nj] += t_up - 1
                    queue.append((ni, nj, t_up - 1))

        # 위쪽 방향
        elif d == 3:
            visited[i - 1][j] = 1
            temperature[i - 1][j] += 5
            queue.append((i - 1, j, 5))

            while queue:
                ci, cj, t_up = queue.popleft()

                if not t_up:
                    continue

                for di, dj in (-1, -1), (-1, 0), (-1, 1):
                    ni, nj = ci + di, cj + dj

                    if ni < 0 or ni == r or nj < 0 or nj == c:
                        continue

                    if visited[ni][nj]:
                        continue

                    if (di, dj) == (-1, 0):
                        if wall[ci][cj][2]:
                            continue

                    elif (di, dj) == (-1, -1):
                        if wall[ci][cj][1] or wall[ni][nj][3]:
                            continue

                    elif (di, dj) == (-1, 1):
                        if wall[ci][cj][0] or wall[ni][nj][3]:
                            continue

                    visited[ni][nj] = 1
                    temperature[ni][nj] += t_up - 1
                    queue.append((ni, nj, t_up - 1))

        # 아래쪽 방향
        elif d == 4:
            visited[i + 1][j] = 1
            temperature[i + 1][j] += 5
            queue.append((i + 1, j, 5))

            while queue:
                ci, cj, t_up = queue.popleft()

                if not t_up:
                    continue

                for di, dj in (1, -1), (1, 0), (1, 1):
                    ni, nj = ci + di, cj + dj

                    if ni < 0 or ni == r or nj < 0 or nj == c:
                        continue

                    if visited[ni][nj]:
                        continue

                    if (di, dj) == (1, 0):
                        if wall[ci][cj][3]:
                            continue

                    elif (di, dj) == (1, -1):
                        if wall[ci][cj][1] or wall[ni][nj][2]:
                            continue

                    elif (di, dj) == (1, 1):
                        if wall[ci][cj][0] or wall[ni][nj][2]:
                            continue

                    visited[ni][nj] = 1
                    temperature[ni][nj] += t_up - 1
                    queue.append((ni, nj, t_up - 1))

    # 온도 조절
    next_temperature = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            next_temperature[i][j] = temperature[i][j]
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj

                if ni < 0 or ni == r or nj < 0 or nj == c:
                    continue

                if (di, dj) == (0, 1):
                    if wall[i][j][0]:
                        continue
                elif (di, dj) == (0, -1):
                    if wall[i][j][1]:
                        continue
                elif (di, dj) == (-1, 0):
                    if wall[i][j][2]:
                        continue
                elif (di, dj) == (1, 0):
                    if wall[i][j][3]:
                        continue

                # 두 칸의 온도 차이
                diff = abs(temperature[i][j] - temperature[ni][nj]) // 4

                # 현재 위치의 온도가 더 크다면 diff만큼 감소
                if temperature[i][j] > temperature[ni][nj]:
                    next_temperature[i][j] -= diff

                # 현재 위치의 온도가 더 작다면 diff만큼 증가
                elif temperature[i][j] < temperature[ni][nj]:
                    next_temperature[i][j] += diff

    # 온도 상태 최신화
    temperature = next_temperature

    ## 1 이상인 바깥 칸의 온도 1 감소
    # 0행과 (r - 1)행
    for j in range(c):
        if temperature[0][j]:
            temperature[0][j] -= 1

        if temperature[r - 1][j]:
            temperature[r - 1][j] -= 1
    
    # 0열과 (c - 1)열
    for i in range(1, r - 1):
        if temperature[i][0]:
            temperature[i][0] -= 1
        if temperature[i][c - 1]:
            temperature[i][c - 1] -= 1

    # 초콜릿 섭취
    chocolate += 1

    # 모든 온도 조사 칸이 조건을 만족하는지 확인
    if check():
        break

print(chocolate)  # 먹은 초콜릿 개수 출력
