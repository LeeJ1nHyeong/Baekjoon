from collections import deque


def bfs():
    if s == 0:  # s == 0인 경우의 예외처리
        return board[x - 1][y - 1]
    
    visited = [[-1] * n for _ in range(n)]
    virus = []  # 바이러스 좌표

    # 바이러스의 좌표를 virus 리스트에 추가
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                visited[i][j] = 0
                virus.append((board[i][j], i, j))

    # 번호가 작은 바이러스부터 퍼지므로 오름차순 정렬
    virus.sort()
    queue = deque(virus)

    # bfs 진행
    while queue:
        v, i, j = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            # 다음 좌표가 탐색을 원하는 좌표일 경우이고 s초 이전이라면 바이러스 번호 return
            if ni == x - 1 and nj == y - 1 and visited[i][j] < s:
                return v
            # s초 이전 미방문 지역에 대해 바이러스 전염 후 queue에 추가
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] == -1 and visited[i][j] < s:
                    visited[ni][nj] = visited[i][j] + 1
                    board[ni][nj] = v
                    queue.append((v, ni, nj))

    return 0  # while문이 종료됐다면 탐색 좌표에 바이러스가 없다는 뜻이므로 0 return


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

print(bfs())
