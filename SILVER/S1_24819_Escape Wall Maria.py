'''
벽에서 가장 빨리 외곽으로 탈출할 수 있는 시간 출력
t시간 안에 탈출 못하면 "NOT POSSIBLE" 출력

0: 이동 가능 공간
1: 벽
U, D, L, R: 해당방향으로부터 이동가능한 공간(ex U의 경우 위에서 오는 방향에서만 이동 가능) 
'''

from collections import deque


def bfs():
    queue = deque()

    for i in range(n):
        for j in range(m):
            if wall[i][j] == "S":
                queue.append((i, j, 0))
                visited[i][j] = 1

    while queue:
        ci, cj, turn = queue.popleft()

        if turn > t:
            continue

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if ni < 0 or ni == n or nj < 0 or nj == m:
                return turn

            if wall[ni][nj] == "1":
                continue

            if visited[ni][nj]:
                continue

            if wall[ni][nj] == "0" or wall[ni][nj] == direction[d]:
                visited[ni][nj] = 1
                queue.append((ni, nj, turn + 1))

    return "NOT POSSIBLE"


t, n, m = map(int, input().split())
wall = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
direction = ["U", "D", "L", "R"]

print(bfs())
