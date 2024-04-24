from collections import deque


def bfs():
    visited = [[0] * m for _ in range(n)]  # 방문 여부 표시용 2차원 리스트

    # 첫번째 행의 "0"인 부분을 시작점으로 bfs 진행
    for j in range(m):
        if board[0][j] == "0":
            queue = deque([(0, j)])
            visited[0][j] = 1

            # bfs
            while queue:
                ci, cj = queue.popleft()

                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == "0":
                        # 다음 좌표가 마지막 행이라면 "YES" return
                        if ni == n - 1:
                            return "YES"
                        # 미방문인 "0"일 경우 방문 표시 후 queue에 좌표 추가
                        if not visited[ni][nj]:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))

    return "NO"  # while문이 종료됐을 경우 전류 침투가 불가능하다는 뜻이므로 "NO" return


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

print(bfs())
