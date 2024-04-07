n, m, a, b = map(int, input().split())
# 장애물을 표시하기 위한 2차원 리스트, 편의를 위해 문제 조건에서 시계 방향 90도 회전한 형태로 진행
board = [[0] * n for _ in range(m)]
items = []  # 아이템 좌표를 저장할 리스트
dp = [[0] * n for _ in range(m)]

# 아이템 좌표 저장
for _ in range(a):
    ax, ay = map(int, input().split())
    items.append((ay - 1, ax - 1))  # 90도 회전한 좌표로 저장

# 장애물 위치 저장
for _ in range(b):
    bx, by = map(int, input().split())
    board[by - 1][bx - 1] = 1

items.sort(key=lambda x: (x[0], x[1]))  # 아이템 좌표를 오름차순으로 정렬

idx_i, idx_j = 0, 0  # 이전 좌표를 저장하기 위한 변수

# 이전 좌표에서 현재 좌표까지를 범위로 지정하여 dp 진행
for idx_a, idx_b in items + [(m - 1, n - 1)]:
    for i in range(idx_i, idx_a + 1):
        for j in range(idx_j, idx_b + 1):
            if i == 0 and j == 0:  # (0, 0) 예외처리
                dp[i][j] = 1
            # 현재 좌표가 장애물이 아닐 경우 이전 좌표들을 더해서 저장
            elif i == 0:
                if not board[i][j]:
                    dp[i][j] = dp[i][j - 1]
            elif j == 0:
                if not board[i][j]:
                    dp[i][j] = dp[i - 1][j]
            else:
                if not board[i][j]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    idx_i, idx_j = idx_a, idx_b  # 현재 좌표를 이전 좌표에 저장

print(dp[m - 1][n - 1])
