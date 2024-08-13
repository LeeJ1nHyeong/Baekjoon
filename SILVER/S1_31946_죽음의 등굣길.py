from collections import deque


def bfs():
    target = board[0][0]

    # bfs 초기 세팅
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        ci, cj = queue.popleft()

        # 목표점에 도착했다면 "ALIVE" return
        if (ci, cj) == (n - 1, m - 1):
            return "ALIVE"
        
        for di in range(-x, x + 1):
            for dj in range(-x, x + 1):
                # 맨해튼 거리 x 이하인 위치 탐색
                if abs(di) + abs(dj) > x:
                    continue

                ni, nj = ci + di, cj + dj

                # 범위 밖을 벗어나면 continue
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue

                # 다른 색깔이라면 continue
                if board[ni][nj] != target:
                    continue

                # 방문 지역이라면 continue
                if visited[ni][nj]:
                    continue

                # 방문 표시 후 queue에 좌표 추가
                visited[ni][nj] = 1
                queue.append((ni, nj))

    return "DEAD"  # while문이 종료됐다면 이동 불가라는 뜻이므로 "DEAD" return


n = int(input())
m = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
x = int(input())

print(bfs())
