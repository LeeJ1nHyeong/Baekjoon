from collections import deque

# 파이어스톰
def fire_storm():
    global board

    # 파이어스톰 시전 단계에 따라 얼음 회전 및 녹기 단계 진행
    for l in l_list:
        board = rotate(l)  # 얼음 회전
        board = melt(board)  # 녹기 단계

    # 파이어 스톰 시전 후 얼음 상태 확인
    ice, max_cnt = 0, 0  # 얼음 총 합, 가장 큰 덩어리(얼음 합)의 칸 개수
    visited = [[0] * (2 ** n) for _ in range(2 ** n)]  # 방문 표시 체크용 2차원 리스트

    # 얼음 탐색
    for i in range(2 ** n):
        for j in range(2 ** n):
            # 시작점을 기준으로 bfs 탐색 진행
            if board[i][j] and not visited[i][j]:
                ice += board[i][j]
                cnt = 1  # 얼음이 차지하는 칸 개수
                queue = deque([(i, j)])
                visited[i][j] = 1

                # bfs 탐색
                while queue:
                    ci, cj = queue.popleft()

                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n and board[ni][nj] and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            cnt += 1
                            ice += board[ni][nj]
                            queue.append((ni, nj))

                max_cnt = max(cnt, max_cnt)  # 얼음 차지 칸 개수 최댓값 여부 확인

    return ice, max_cnt  # 얼음 총 합, 가장 큰 얼음 덩어리의 칸 개수 return

# 90도 회전 단계
def rotate(l):
    rotate_board = [[0] * (2 ** n) for _ in range(2 ** n)]

    for i in range(0, 2 ** n, 2 ** l):
        for j in range(0, 2 ** n, 2 ** l):
            rotate_part(i, j, 2 ** l, rotate_board)

    return rotate_board

# 부분별 회전
def rotate_part(r, c, l, lst):
    for i in range(l):
        for j in range(l):
            lst[r + j][c + (l - 1) - i] = board[r + i][c + j]

# 녹기 단계
def melt(lst):
    melt_board = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(2 ** n):
        for j in range(2 ** n):
            if not lst[i][j]:
                continue
            melt_board[i][j] = lst[i][j]
            cnt = 0
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n and lst[ni][nj]:
                    cnt += 1

            if cnt < 3:
                melt_board[i][j] -= 1

    return melt_board


n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** n)]
l_list = list(map(int, input().split()))

ice, max_cnt = fire_storm()  # 얼음 총 합, 가장 큰 덩어리(얼음 합)의 칸 개수

# 얼음 총 합, 가장 큰 얼음 덩어리의 칸 개수 출력
print(ice)
print(max_cnt)
