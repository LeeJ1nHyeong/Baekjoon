''' 문제 설명
+ : 4방향 이동 가능
- : 좌우 이동 가능
| : 상하 이동 가능
* : 벽 (이동 불가)
시작점(0, 0), 끝점(r - 1, c - 1) 포함 이동 거리 최솟값 출력
'''

from collections import deque


def bfs():
    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1
    queue = deque([(0, 0, 1)])

    # bfs 진행
    while queue:
        i, j, move = queue.popleft()
        # 도착점이라면 이동 거리 return
        if i == r - 1 and j == c - 1:
            return move
        
        # 좌우 이동
        if board[i][j] == "+" or board[i][j] == "-":
            for di, dj in (0, 1), (0, -1):
                ni, nj = i + di, j + dj
                if 0 <= ni < r and 0 <= nj < c and board[ni][nj] != "*" and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, move + 1))

        # 상하 이동
        if board[i][j] == "+" or board[i][j] == "|":
            for di, dj in (1, 0), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < r and 0 <= nj < c and board[ni][nj] != "*" and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, move + 1))

    return -1  # while문이 종료됐다면 이동 불가이므로 -1 return


t = int(input())

for _ in range(t):
    r = int(input())
    c = int(input())
    board = [list(input()) for _ in range(r)]
    print(bfs())
