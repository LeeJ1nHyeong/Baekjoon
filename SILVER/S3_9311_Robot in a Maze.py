from collections import deque

def bfs():
    queue = deque()

    for i in range(r):
        for j in range(c):
            if board[i][j] == "S":
                queue.append((i, j, 0))
                visited[i][j] = 1

    while queue:
        ci, cj, move = queue.popleft()

        # 현재 위치가 출구라면 최소 이동 횟수를 출력 형식에 맞게 return
        if board[ci][cj] == "G":
            return f"Shortest Path: {move}"
        
        # 상하좌우 4방향 탐색
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni == r or nj < 0 or nj == c:
                continue

            if board[ni][nj] == "X":
                continue

            if visited[ni][nj]:
                continue

            # 이동 가능 조건이라면 방문 표시 후 queue에 좌표 추가
            visited[ni][nj] = 1
            queue.append((ni, nj, move + 1))

    return "No Exit"  # 출구로 이동 불가라면 "No Exit" return


t = int(input())

for _ in range(t):
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]
    visited = [[0] * c for _ in range(r)]

    print(bfs())
