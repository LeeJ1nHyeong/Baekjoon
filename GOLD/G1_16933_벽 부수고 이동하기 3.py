'''
1. 파괴한 벽 개수에 따른 방문 표시용 3차원 배열 생성
2. 처음 좌표(벽 개수 0)에 방문 표시 후 bfs 진행
3. 낮밤 여부(이동 횟수 % 2)에 따라 조건 다르게 해서 진행
    3-1. 낮밤 여부 상관 없이 다음 좌표가 이동 가능(0)이라면 다음 좌표 방문표시 후 queue에 좌표 추가
    3-2. 낮일 경우(이동 횟수 % 2 == 1)에 다음 좌표가 벽(1)이고 최대 벽 개수를 넘기지 않는다면 다음 좌표 방문표시 후 queue에 좌표 추가
    3-3. 밤일 경우(이동 횟수 % 2 == 0)에 다음 좌표가 벽(1)이라면, 이동횟수를 1 증가시키고 현재 좌표를 queue에 추가
4. 목적지에 도착했을 경우 이동 횟수(move)값 return, 목적지에 도착을 못했다면 -1 return
'''

from collections import deque

def bfs():
    queue = deque([(0, 0, 1, 0)])  # i, j, 이동 횟수, 벽 개수

    while queue:
        i, j, move, broken = queue.popleft()
        if i == n - 1 and j == m - 1:
            return move

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            # 낮밤 여부에 따라 조건을 다르게 하면서 진행
            if 0 <= ni < n and 0 <= nj < m:
                # 낮
                if move % 2:
                    # 다음 좌표가 0일 경우
                    if board[ni][nj] == "0" and not visited[ni][nj][broken]:
                        visited[ni][nj][broken] = 1
                        queue.append((ni, nj, move + 1, broken))
                    # 다음 좌표가 1(벽)일 경우
                    elif board[ni][nj] == "1" and broken < k and not visited[ni][nj][broken + 1]:
                        visited[ni][nj][broken + 1] = 1
                        queue.append((ni, nj, move + 1, broken + 1))

                # 밤
                else:
                    # 다음 좌표가 0일 경우
                    if board[ni][nj] == "0" and not visited[ni][nj][broken]:
                        visited[ni][nj][broken] = 1
                        queue.append((ni, nj, move + 1, broken))
                    # 다음 좌표가 1(벽)일 경우
                    elif board[ni][nj] == "1" and broken < k and not visited[ni][nj][broken + 1]:
                        queue.append((i, j, move + 1, broken))

    return -1

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]  # 벽 파괴 개수에 따른 방문표시용 3차원 배열
visited[0][0][0] = 1

print(bfs())