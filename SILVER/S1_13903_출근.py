from collections import deque


def bfs():
    visited = [[0] * c for _ in range(r)]  # 방문 여부 체크용 2차원 리스트
    queue = deque()
    # 첫 행의 세로 블록 좌표를 queue에 추가
    for j in range(c):
        if board[0][j]:
            visited[0][j] = 1
            queue.append((0, j, 0))

    # r이 1일 경우의 예외처리
    # 세로 블록이 존재할 경우 0 return
    if r == 1 and queue:
        return 0
    
    # bfs 진행
    while queue:
        ci, cj, cnt = queue.popleft()

        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < r and 0 <= nj < c and board[ni][nj]:
                # 다음 이동 지역이 r행이라면 cnt + 1을 return
                if ni == r - 1:
                    return cnt + 1
                # 미방문 지역의 좌표를 queue에 추가
                if not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, cnt + 1))

    return -1  # while문이 종료됐다면 r행까지 이동하는 방법이 없으므로 -1 return


r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

# 이동 방법을 d에 담기
d = []
n = int(input())

for _ in range(n):
    r2, c2 = map(int, input().split())
    d.append((r2, c2))

print(bfs())
