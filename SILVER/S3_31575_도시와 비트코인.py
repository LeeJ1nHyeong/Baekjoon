from collections import deque


def bfs():
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        ci, cj = queue.popleft()

        # 거래소에 도착했다면 "Yes" return
        if (ci, cj) == (n - 1, m - 1):
            return "Yes"
        
        # 오른쪽과 아래쪽으로만 이동 가능
        for di, dj in (0, 1), (1, 0):
            ni, nj = ci + di, cj + dj

            if ni == n or nj == m:
                continue

            if not board[ni][nj]:
                continue

            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj))

    return "No"


m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs())
