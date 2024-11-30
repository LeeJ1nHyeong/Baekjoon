'''
시작지점(S)부터 d개(1 ~ d)의 체크포인트를 순서대로 모두 방문 후 도착지점(E)에 도착하는 최소 이동 거리 출력

# : 벽
S, E, . : 이동 가능 구역
1 ~ 9 : 체크포인트

'''

from collections import deque


def bfs():
    visited = [[[0 for _ in range(d + 1)] for _ in range(c)] for _ in range(r)]
    queue = deque()

    # 시작지점 탐색
    for i in range(r):
        for j in range(c):
            if maze[i][j] == "S":
                visited[i][j][0] = 1
                queue.append((i, j, 0, 0))

    while queue:
        ci, cj, checkpoint, move = queue.popleft()  # 좌표, 현재까지 방문한 체크포인트, 이동 횟수

        # 모든 체크포인트를 방문하고 도착지점에 도착했다면 이동횟수 return
        if maze[ci][cj] == "E" and checkpoint == d:
            return move

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == r or nj < 0 or nj == c:
                continue

            if maze[ni][nj] == "#":
                continue

            # 현재 위치가 다음 체크포인트라면 체크포인트 방문 표시 후 queue에 추가
            if maze[ni][nj].isdigit() and int(maze[ni][nj]) == checkpoint + 1:
                visited[ni][nj][checkpoint + 1] = 1
                queue.append((ni, nj, checkpoint + 1, move + 1))

            else:
                if visited[ni][nj][checkpoint]:
                    continue

                visited[ni][nj][checkpoint] = 1
                queue.append((ni, nj, checkpoint, move + 1))


t = int(input())

for _ in range(t):
    r, c, d = map(int, input().split())
    maze = [list(input()) for _ in range(r)]

    print(bfs())
