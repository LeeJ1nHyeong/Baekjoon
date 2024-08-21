from collections import deque


def bfs():
    visited = [[0] * n for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        ci, cj = queue.popleft()

        # 목표 지점에 도착했다면 "HaruHaru" return
        if board[ci][cj] == -1:
            return "HaruHaru"

        move = board[ci][cj]  # 이동 칸 수

        # 현재 위치에서 오른쪽, 아래 방향에 이동할 곳이 있는지 탐색
        for di, dj in (0, move), (move, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

    return "Hing"  # while 문이 종료됐다면 도착 불가라는 뜻이므로 "Hing" return


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs())
