'''
좌상단("s")에서 우하단("d")까지 이동할 수 있는 최단거리 출력

인접 4방향으로 이동 가능, 소행성으로는 이동불가

목적지까지 이동이 불가능하다면 -1 출력

"*" : 소행성
"-" : 이동 가능 공간
'''

from collections import deque


def bfs():
    visited = [[0] * n for _ in range(n)]
    queue = deque([(0, 0, 0)])
    visited[0][0] = 1

    while queue:
        ci, cj, move = queue.popleft()

        if board[ci][cj] == "d":
            return move

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == n or nj < 0 or nj == n:
                continue

            if board[ni][nj] == "*":
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))

    return -1


t = int(input())

for _ in range(t):
    n = int(input())
    board = [list(input()) for _ in range(n)]

    print(bfs())
