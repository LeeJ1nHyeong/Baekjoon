# 땅이 물에 가라앉는지 여부 확인
def check(i, j):
    cnt = 0  # 바다 개수

    # 현재 위치 기준 4방향을 탐색
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj

        # 지도 밖을 벗어나면 cnt 1 추가 후 continue
        if ni < 0 or ni == r or nj < 0 or nj == c:
            cnt += 1
            continue

        # 바다일 경우 cnt 1 추가
        if board[ni][nj] == ".":
            cnt += 1

    # 바다 개수가 3개 이상이라면 False return
    if cnt >= 3:
        return False

    return True  # 아니라면 True return


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]  # 현재 지도
board_50y = [["."] * c for _ in range(r)]  # 50년 뒤 지도
min_i, max_i, min_j, max_j = r, 0, c, 0  # 출력할 지도 범위

for i in range(r):
    for j in range(c):
        # 땅인 곳의 주변 바다를 탐색하여 땅이 잠기지 않을 경우 50년 뒤 지도에 땅 표시
        if board[i][j] == "X" and check(i, j):
            board_50y[i][j] = "X"
            # 출력 지도 범위 설정
            min_i = min(i, min_i)
            max_i = max(i, max_i)
            min_j = min(j, min_j)
            max_j = max(j, max_j)

# 형식에 맞게 지도 출력
for i in range(min_i, max_i + 1):
    print("".join(board_50y[i][min_j: max_j + 1]))
