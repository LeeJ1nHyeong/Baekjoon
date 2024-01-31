from collections import deque

def bfs():
    if n == 1 and m == 1:  # n, m == 1, 1일 경우의 예외처리
        return 1

    queue = deque([(0, 0, 1, 0)])  # (i, j, 이동 거리, 부순 벽 개수)
                                   # 시작 좌표도 이동 거리에 포함하기 때문에 1로 시작
    
    # bfs 진행
    while queue:
        i, j, move, broken = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if ni == n - 1 and nj == m - 1:  # 다음 좌표가 목적지라면 return
                    return move + 1
                if board[ni][nj] == "0" and not visited[ni][nj][broken]:
                    visited[ni][nj][broken] = 1  # 부순 벽 개수에 따라 방문 표시 좌표를 다르게 지정
                    queue.append((ni, nj, move + 1, broken))
                elif board[ni][nj] == "1" and broken < k:  # 벽 파괴 가능 개수를 넘기지 않았다면 부순 벽 개수를 1 증가
                    if not visited[ni][nj][broken + 1]:
                        visited[ni][nj][broken + 1] = 1
                        queue.append((ni, nj, move + 1, broken + 1))

    return -1  # while문 종료라면 목적지 도착을 못했다는 뜻이므로 -1 return

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]  # 부순 벽 횟수에 따른 방문여부 체크용 3차원 배열
visited[0][0][0] = 1  # 처음 좌표 방문 표시

print(bfs())