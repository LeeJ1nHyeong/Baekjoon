n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cloud = [[0] * n for _ in range(n)]  # 구름의 위치

# 구름 초기 위치 저장
cloud[n - 2][0], cloud[n - 1][0] = 1, 1
cloud[n - 2][1], cloud[n - 1][1] = 1, 1

# 9시 방향부터 시계방향
di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]


# 구름 이동
def move_cloud():
    next_cloud = [[0] * n for _ in range(n)]

    # 범위를 벗어나면 반대편으로 이동
    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                next_cloud[(i + di[d] * s) % n][(j + dj[d] * s) % n] = 1

    return next_cloud


# 비 내리기
def rain():
    # 구름이 이동한 위치에 물 1 증가
    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                board[i][j] += 1


# 물 복사 버그 마법
def water_copy_bug():
    next_board = [[0] * n for _ in range(n)]

    # 물 증가한 위치 기준 대각선 4방향에 물이 존재하는 곳의 개수만큼 증가
    for i in range(n):
        for j in range(n):
            if not cloud[i][j]:
                next_board[i][j] = board[i][j]

            else:
                cnt = 0

                # 현재 위치 기준 대각선 4방향 탐색
                for cdi, cdj in (-1, -1), (-1, 1), (1, 1), (1, -1):
                    ni, nj = i + cdi, j + cdj

                    # 범위를 벗어나는 곳은 제외
                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        continue

                    if not board[ni][nj]:
                        continue

                    cnt += 1

                next_board[i][j] = board[i][j] + cnt

    return next_board


# 구름 생성
def make_cloud():
    for i in range(n):
        for j in range(n):
            # 이전에 구름이 있었던 위치는 구름 제거만 진행
            if cloud[i][j]:
                cloud[i][j] = 0
                continue

            # 구름이 없었던 위치 중 물이 2 이상인 곳의 물이 2 줄어들고 그 위치에 구름 생성
            if board[i][j] < 2:
                continue

            board[i][j] -= 2
            cloud[i][j] = 1


for _ in range(m):
    d, s = map(int, input().split())

    # 구름 이동
    cloud = move_cloud()

    # 비 내리기
    rain()

    # 물 복사 버그 마법 시전
    board = water_copy_bug()

    # 구름 생성
    make_cloud()

# 모든 이동 종료 후 물의 양 합 출력
ans = 0
for b in board:
    ans += sum(b)

print(ans)