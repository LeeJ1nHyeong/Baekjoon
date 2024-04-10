from collections import deque


def bfs():
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]  # 벽 파괴 여부까지 반영한 방문 체크용 3차원 리스트
    visited[hi - 1][hj - 1][0] = 1  # 시작 좌표 방문 표시
    queue = deque([(hi - 1, hj - 1, 0, 0)])  # 시작 좌표, 이동 횟수, 벽 파괴 여부를 튜플 형태로 queue에 추가

    # bfs 진행
    while queue:
        i, j, move, wall = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                # 다음 좌표가 도착지점이라면 이동 횟수 + 1을 return
                if ni == ei - 1 and nj == ej - 1:
                    return move + 1
                
                # 다음 좌표가 통로(0)인 미방문 좌표일 경우, 방문 표시 후 queue에 추가
                if board[ni][nj] == 0 and not visited[ni][nj][wall]:
                    visited[ni][nj][wall] = 1
                    queue.append((ni, nj, move + 1, wall))
                    
                # 다음 좌표가 벽(1)일 경우, 벽 파괴 횟수가 0이라면 벽 파괴 후 queue에 추가
                else:
                    if not wall and not visited[ni][nj][1]:
                        visited[ni][nj][1] = 1
                        queue.append((ni, nj, move + 1, 1))

    return -1  # while문이 종료됐다면 탈출 불가이므로 -1 return


n, m = map(int, input().split())
hi, hj = map(int, input().split())
ei, ej = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs())
