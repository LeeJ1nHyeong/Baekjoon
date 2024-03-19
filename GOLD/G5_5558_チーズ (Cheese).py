from collections import deque


def bfs(ti, tj, target):
    queue = deque()
    visited = [[0] * w for _ in range(h)]  # 방문 표시용 2차원 리스트
    # 시작 위치 작업
    queue.append((ti, tj, 0))  # 시작 좌표, 이동 횟수
    visited[ti][tj] = 1

    # bfs 진행
    while queue:
        i, j, cnt = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w:
                # 다음 좌표가 target 번호라면 이동 횟수, 다음 좌표 return
                if board[ni][nj] == str(target + 1):
                    return cnt + 1, ni, nj
                # 벽("X")이 아닌 미방문 좌표는 방문 표시 후 queue에 추가
                if board[ni][nj] != "X" and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, cnt + 1))


h, w, n = map(int, input().split())
board = [list(input()) for _ in range(h)]

cnt, ti, tj = 0, 0, 0  # 이동 횟수, 현재 좌표

# 시작점 좌표를 찾아 현재 좌표로 저장
for i in range(h):
    for j in range(w):
        if board[i][j] == "S":
            ti, tj = i, j
            break

# 현재 위치에서 다음 target 번호까지 bfs로 이동
for i in range(n):
    move, ni, nj = bfs(ti, tj, i)
    # 이동 후 현재 좌표 갱신 및 이동 횟수 더하기
    ti, tj = ni, nj
    cnt += move

print(cnt)
