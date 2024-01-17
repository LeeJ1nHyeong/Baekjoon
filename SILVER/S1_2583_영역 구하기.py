from collections import deque

def bfs(i, j):  # 영역의 넓이를 구하기 위한 bfs
    queue = deque([(i, j)])  # 시작 좌표를 큐에 담은 상태로 시작

    # 방문 표시 및 넓이 카운트 1 추가
    board[i][j] = 1
    cnt = 1

    # 4방향 델타 탐색을 진행하여 해당 영역의 넓이를 구함
    while queue:
        now_i, now_j = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = now_i + di, now_j + dj
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 0:
                board[ni][nj] = 1
                cnt += 1
                queue.append((ni, nj))

    return cnt  # 탐색 완료 후 넓이값을 return

m, n, k = map(int, input().split())
board = [[0] * m for _ in range(n)]  # 모눈종이
area = []  # 각 영역의 넓이를 담을 리스트

# 직사각형 내부를 -1로 구분
for _ in range(k):
    si, sj, ei, ej = map(int, input().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            board[i][j] -= 1

# 분리된 영역(0)을 찾으면 그 좌표를 시작으로 bfs 진행 후 return값을 area 리스트에 추가
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            area.append(bfs(i, j))

area.sort()  # 오름차순 정렬

print(len(area))
print(*area)