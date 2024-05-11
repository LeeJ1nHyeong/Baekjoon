from collections import deque


def bfs():
    # bfs 초기 설정
    board = [[0] * n for _ in range(n)]
    board[r1][c1] = 1
    queue = deque([(r1, c1, 0)])  # 시작 좌표, 이동 횟수를 튜플 형태로 queue에 저장

    # bfs 진행
    while queue:
        r, c, move = queue.popleft()
        # 현재 좌표가 도착점이라면 이동 횟수 return
        if r == r2 and c == c2:
            return move
        
        # 문제에 제시된 이동 방법을 활용하여 탐색
        for dr, dc in (-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc]:
                board[nr][nc] = 1
                queue.append((nr, nc, move + 1))

    return -1  # while문이 종료됐다면 이동 불가라는 뜻이므로 -1 return


n = int(input())
r1, c1, r2, c2 = map(int, input().split())

print(bfs())
