'''
1. 각 나라별 인구를 기준으로 bfs를 진행하여 개방을 하는 나라끼리 visited에 같은 값(idx)으로 저장
    1-1. 이 때 idx값이 n * n이라면 개방하는 곳이 없으므로 while문 종료
2. 각 영역별로 visited 값이 같은 나라끼리 bfs를 진행하여 인구의 합(total)과 나라 수(cnt)를 계산하여 total / cnt를 새롭게 저장
3. 일 수(days)를 1 증가하고 위 과정 반복
'''

from collections import deque
import sys
input = sys.stdin.readline


def search(i, j, idx):  # 인구 개방여부 탐색
    queue = deque([(i, j)])

    while queue:
        now_i, now_j = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = now_i + di, now_j + dj
            if 0 <= ni < n and 0 <= nj < n:
                # 인구 차이 조건이 성립되면 해당 나라의 visited를 idx로 저장하고 queue에 좌표 추가
                if not visited[ni][nj] and l <= abs(board[now_i][now_j] - board[ni][nj]) <= r:
                    visited[ni][nj] = idx
                    queue.append((ni, nj))


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
days = 0  # 인구 이동 일 수

# 인구 이동
while True:
    visited = [[0] * n for _ in range(n)]  # 인구 개방을 한 나라끼리의 영역을 저장

    idx = 0  # 영역 번호
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                idx += 1
                visited[i][j] = idx
                search(i, j, idx)

    if idx == n * n:  # idx가 n * n이라면 인구 개방이 없다는 뜻이므로 while문 종료
        break

    # 개방한 나라끼리 인구 이동 진행
    visited2 = [[0] * n for _ in range(n)]  # 인구를 개방하는 나라끼리 계산을 하기 위한 방문 여부 체크용 리스트
    for i in range(n):
        for j in range(n):
            if not visited2[i][j]:
                visited2[i][j] = 1
                idx = visited[i][j]  # 인구 이동을 진행하는 영역 번호
                queue = deque([(i, j)])
                idx_list = [(i, j)]  # 인구 이동을 한 나라의 좌표를 저장
                cnt = 1  # 인구 이동을 진행하는 나라의 개수
                total = board[i][j]  # 인구 이동을 진행하는 나라끼리의 총 인구 수

                # bfs 진행
                while queue:
                    now_i, now_j = queue.popleft()
                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = now_i + di, now_j + dj
                        if 0 <= ni < n and 0 <= nj < n and not visited2[ni][nj]:
                            if idx == visited[ni][nj]:
                                cnt += 1
                                total += board[ni][nj]
                                visited2[ni][nj] = 1
                                queue.append((ni, nj))
                                idx_list.append((ni, nj))

                # 총 인구 수를 나라 수에 나눈 값을 각 나라에 저장
                for idx_i, idx_j in idx_list:
                    board[idx_i][idx_j] = total // cnt

    days += 1  # 인구 이동 종료 후 일 수 1 증가

print(days)  # 인구 이동 일 수 출력