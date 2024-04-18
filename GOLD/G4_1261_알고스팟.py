import heapq


def dijkstra():
    visited = [[0] * m for _ in range(n)]  # 방문 여부 체크용 2차원 리스트
    visited[0][0] = 1  # 시작점 방문 표시
    # 다익스트라에 사용될 우선순위 큐
    queue = []
    heapq.heappush(queue, (0, 0, 0))

    # 다익스트라 진행
    while queue:
        wall, i, j = heapq.heappop(queue)
        # 도착점이라면 벽 파괴 횟수 return
        if i == n - 1 and j == m - 1:
            return wall
        
        # 미방문 지역 탐색
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = 1
                # 벽이 아니라면 파괴한 벽 개수 그대로 좌표와 함께 queue에 저장
                if maze[ni][nj] == "0":
                    heapq.heappush(queue, (wall, ni, nj))
                # 벽이라면 파괴한 벽 개수를 1 증가 후 좌표와 함께 queue에 저장
                elif maze[ni][nj] == "1":
                    heapq.heappush(queue, (wall + 1, ni, nj))


m, n = map(int, input().split())
maze = [list(input()) for _ in range(n)]

print(dijkstra())
