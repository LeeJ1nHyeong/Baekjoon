from collections import deque


def check(ci, cj, i, j, target):  # 다음 좌표의 4방향을 탐색할 함수
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        # 이동 전 좌표의 visited값이 ni, nj의 visited값과 같고 target과 값이 다를 경우 True return
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == visited[ci][cj]:
            if (target == 1 and board[ni][nj] == 2) or (target == 2 and board[ni][nj] == 1):
                return True

    return False  # for문이 종료됐다면 3번 바이러스 변환 조건이 아니므로 False return


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]  # 바이러스 감염 시간을 저장할 2차원 리스트

virus = [0] * 4  # 바이러스 개수

queue = deque()

# 처음 1번, 2번 바이러스의 좌표를 queue에 저장
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 or board[i][j] == 2:
            virus[board[i][j]] += 1
            visited[i][j] = 0
            queue.append((i, j, board[i][j]))

# bfs 진행
while queue:
    ci, cj, target = queue.popleft()
    # 현재 좌표가 3번 바이러스 감염지역이라면 continue
    if board[ci][cj] == 3:
        continue
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        # 백신(-1)이 없는 지역 탐색
        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != -1:
            if board[ni][nj] == 0:
                # 다음 좌표의 4방향을 탐색하여 같은 시간에 감염된 다른 번호의 바이러스가 있다면 3번 바이러스 감염
                if check(ci, cj, ni, nj, target):
                    board[ni][nj] = 3
                    virus[3] += 1
                # 3번 바이러스 조건에 부합하지 않다면 현재 바이러스가 감염
                else:
                    board[ni][nj] = target
                    visited[ni][nj] = visited[ci][cj] + 1
                    virus[target] += 1
                    queue.append((ni, nj, target))

print(*virus[1:])  # 1, 2, 3번 바이러스 감염 지역 개수 출력
