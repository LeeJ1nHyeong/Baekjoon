def search(i, j):  # 4방향 탐색
    # 현재 좌표의 4방향 중 갈 곳이 하나라도 있다면 True, 하나도 없다면 False return
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c:
            if not board[ni][nj]:
                return True

    return False


r, c = map(int, input().split())
board = [[0] * c for _ in range(r)]  # 로봇이 이동하는 맵

# 4방향 델타탐색을 위한 좌표 리스트
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

# 장애물을 board에 표시
k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    board[br][bc] = 1

sr, sc = map(int, input().split())  # 로봇 좌표
board[sr][sc] = 1  # 시작 좌표 방문 처리
order = list(map(int, input().split()))  # 방향 순서
order_idx = 0  # 현재 방향을 나타내기 위한 인덱스

while True:
    # 현재 좌표에서 더 이상 갈 곳이 없다면 while문 종료
    if not search(sr, sc):  
        break

    # 현재 진행 방향부터 방향 순서별로 이동할 수 있는 좌표가 있을 때 까지 for문 진행
    for i in range(4):
        o = order[(order_idx + i) % 4]
        nr, nc = sr + dr[o], sc + dc[o]
        if 0 <= nr < r and 0 <= nc < c and not board[nr][nc]:
            order_idx += i
            board[nr][nc] = 1
            sr, sc = nr, nc
            break

print(sr, sc)  # 이동 후 최종 로봇 좌표 출력