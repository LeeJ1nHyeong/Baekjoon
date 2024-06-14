from collections import deque


def search():
    # 가장 큰 블록 그룹인지 확인
    def check():
        if block_cnt < max_block_cnt:
            return False

        if block_cnt == max_block_cnt:
            if rainbow_cnt < max_rainbow_cnt:
                return False

            if rainbow_cnt == max_rainbow_cnt:
                if center_i < max_i:
                    return False

                if center_i == max_i:
                    if center_j < max_j:
                        return False

        return True

    max_block_cnt = 0  # 최대 블록 개수
    max_rainbow_cnt = 0  # 최대 블록 그룹일 때의 무지개 블록 개수
    max_i, max_j = -1, -1  # 최대 블록 그룹일 때의 기준점 좌표

    visited = [[0] * n for _ in range(n)]  # 방문 여부

    for i in range(n):
        for j in range(n):
            # 무지개 블록(0)이나 검은색 블록(-1)은 제외
            if board[i][j] <= 0:
                continue

            # 빈 칸(m + 1)은 제외
            if board[i][j] == m + 1:
                continue

            # 방문 지역은 제외
            if visited[i][j]:
                continue

            # 무지개 블록 방문 기록 초기화
            for ri, rj in rainbow:
                visited[ri][rj] = 0

            # bfs 초기 세팅
            target = board[i][j]
            queue = deque([(i, j)])
            visited[i][j] = 1

            block_cnt = 1
            rainbow_cnt = 0
            center_i, center_j = i, j

            # bfs 진행
            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj

                    # 탐색 조건을 충족하지 못했다면 continue
                    if not bfs_check(target, ni, nj, visited):
                        continue

                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                    block_cnt += 1

                    # 무지개 블록이면 rainbow_cnt 1 추가
                    if not board[ni][nj]:
                        rainbow_cnt += 1

                    # 기준점 체크
                    else:
                        if ni > center_i:
                            continue

                        if ni == center_i:
                            if nj > center_j:
                                continue

                        center_i, center_j = ni, nj

            # 블록 개수가 2개 미만이면 continue
            if block_cnt < 2:
                continue

            # 가장 큰 블록 그룹인지 확인
            if check():
                max_block_cnt = block_cnt
                max_rainbow_cnt = rainbow_cnt
                max_i, max_j = center_i, center_j

    return max_i, max_j, max_block_cnt


# bfs 탐색 요건
def bfs_check(target, ni, nj, visited):
    # 범위를 벗어나면 False return
    if ni < 0 or ni == n or nj < 0 or nj == n:
        return False

    # 타겟 블록이 아니고 무지개 블록이 아니면 False return
    if board[ni][nj] != target and board[ni][nj] != 0:
        return False

    # 방문 지역이라면 False return
    if visited[ni][nj]:
        return False

    return True  # 모든 조건을 만족한다면 True return


# 블록 제거
def delete_block():
    target = board[max_i][max_j]
    board[max_i][max_j] = m + 1
    visited = [[0] * n for _ in range(n)]

    # bfs
    queue = deque([(max_i, max_j)])
    visited[max_i][max_j] = 1

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if not bfs_check(target, ni, nj, visited):
                continue

            board[ni][nj] = m + 1
            visited[ni][nj] = 1
            queue.append((ni, nj))


# 중력 작용
def gravity():
    for j in range(n):
        move = 0
        for i in range(n - 1, -1, -1):
            if board[i][j] == m + 1:
                move += 1
            else:
                # 검은색 블록은 중력에 영향받지 않음
                if board[i][j] == -1:
                    move = 0
                else:
                    if move:
                        board[i + move][j] = board[i][j]
                        board[i][j] = m + 1


# 반시계 방향 90도 회전
def rotate():
    global board

    next_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            next_board[n - 1 - j][i] = board[i][j]

    board = next_board


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

score = 0  # 점수

# 빈칸은 m + 1로 구현
while True:
    # 무지개 블록 탐색
    rainbow = []

    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                rainbow.append((i, j))

    # 크기가 큰 블록 그룹 탐색
    max_i, max_j, max_block_cnt = search()

    # 블록 그룹이 없으면 while문 종료
    if (max_i, max_j) == (-1, -1):
        break

    # 점수 추가
    score += max_block_cnt ** 2

    # 블록 제거
    delete_block()

    # 중력 작용
    gravity()

    # 90도 반시계 방향 회전
    rotate()

    # 회전 후 중력 작용
    gravity()

print(score)  # 점수 출력
