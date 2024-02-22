from collections import deque


def bfs():  # bfs
    if w == 1 and h == 1:  # 1X1일 경우에 대한 예외처리
        return 0
    
    # bfs 초기 세팅
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 0

    # bfs 진행
    while queue:
        i, j, horse = queue.popleft()  # i, j좌표, 말 이동 사용 횟수

        # 일반 이동
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if ni == h - 1 and nj == w - 1:  # 다음 위치가 도착지점이라면 return
                return visited[i][j][horse] + 1

            if 0 <= ni < h and 0 <= nj < w:
                if not board[ni][nj] and visited[ni][nj][horse] == -1:
                    visited[ni][nj][horse] = visited[i][j][horse] + 1
                    queue.append((ni, nj, horse))

        # 말 이동
        if horse < k:
            for di, dj in (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1):
                ni, nj = i + di, j + dj
                if ni == h - 1 and nj == w - 1:  # 다음 위치가 도착지점이라면 return
                    return visited[i][j][horse] + 1

                if 0 <= ni < h and 0 <= nj < w:
                    if not board[ni][nj] and visited[ni][nj][horse + 1] == -1:
                        visited[ni][nj][horse + 1] = visited[i][j][horse] + 1
                        queue.append((ni, nj, horse + 1))

    return -1


k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

# 말 이동 사용 횟수를 같이 체크하기 위한 방문 여부 체크용 3차원 리스트
visited = [[[-1 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]

print(bfs())