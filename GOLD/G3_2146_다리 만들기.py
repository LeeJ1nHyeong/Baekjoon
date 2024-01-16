'''
1. 섬 구분을 위해 -1부터 1씩 감소하는 값으로 bfs 진행 (island 함수 실행)
2. 각 섬에서 4방향 델타탐색을 진행하여 해당 위치가 바다일 경우(0일 경우) 그 좌표를 기준으로 다리를 놓는 bfs 진행(bridge 함수 실행)
    2-1. 큐(queue2)에 첫 위치 좌표와 cnt 1을 tuple형태로 추가한 뒤 bfs 진행
    2-2. 다음 진행방향이 0이고 cnt가 최솟값 미만이면 해당 좌표 방문 표시 후 같은 tuple형태로 큐에 추가
    2-3. 다음 진행방향이 섬일 경우, 최솟값 비교 후 bfs 종료
'''
from collections import deque

def island(i, j, island_num):  # 섬 구분을 위한 bfs 함수(i좌표, j좌표, 섬 번호)
    queue = deque([(i, j)])  # 첫 좌표를 큐에 담은 상태로 시작

    while queue:
        now_i, now_j = queue.popleft()
        board[now_i][now_j] = island_num  # 해당 위치에 섬 번호를 저장
        # 4방향 델타 탐색
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = now_i + di, now_j + dj
            # 이어져 있는 섬의 좌표에 섬 번호 저장 후 큐에 추가
            if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 1:
                board[ni][nj] = island_num
                queue.append((ni, nj))

def bridge(i, j, island_num):  # 다리 짓기 bfs(출발 i좌표, 출발 j좌표, 출발 섬 번호)
    global min_cnt

    queue2 = deque([(i, j, 1)])
    visited = [[0] * n for _ in range(n)]  # 메모리 절약을 위해 방문 표시 리스트 추가
    visited[i][j] = 1

    while queue2:
        now_i, now_j, cnt = queue2.popleft()  # 현재 i, j 좌표, 이동 횟수 
        # 4방향 델타 탐색
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = now_i + di, now_j + dj
            if 0 <= ni < n and 0 <= nj < n:
                # 다음 진행방향이 바다이고 다음 이동 횟수가 최솟값 미만이며 미방문이라면 방문 표시 후 큐에 추가
                if board[ni][nj] == 0 and cnt + 1 < min_cnt and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue2.append((ni, nj, cnt + 1))
                # 다음 진행방향이 출발 섬이 아닌 섬이라면 최솟값 비교 후 bfs 종료
                elif board[ni][nj] < 0 and board[ni][nj] != island_num:
                    min_cnt = min(cnt, min_cnt)
                    return

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

island_num = 0  # 섬 번호
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            island_num -= 1  # 원활한 구분을 위해 음수 값으로 구분 진행
            board[i][j] = island_num
            island(i, j, island_num)

min_cnt = n * n

for i in range(n):
    for j in range(n):
        # 해당 좌표가 섬이고 4방향 탐색한 위치가 바다라면 그 좌표에서 bfs 진행
        if board[i][j] != 0:
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
                    bridge(ni, nj, board[i][j])

print(min_cnt)