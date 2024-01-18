def move():  # 파이어볼 이동
    next_board = [[[] for _ in range(n)] for _ in range(n)]  # 이동 후
    for i in range(n):
        for j in range(n):
            # 해당 좌표에 파이어볼이 있다면 각 파이어볼을 d방향으로 s만큼 이동
            if board[i][j]:
                while board[i][j]:
                    m, s, d = board[i][j].pop()
                    ni = (i + di[d] * s) % n
                    nj = (j + dj[d] * s) % n
                    next_board[ni][nj].append((m, s, d))  # 이동 후 좌표에 파이어볼 추가

    return next_board

def fireball():  # 파이어볼 이동 후 조치
    for i in range(n):
        for j in range(n):
            length = len(next_board[i][j])
            # 해당 좌표의 파이어볼이 1개 이하일 경우
            if length <= 1:
                board[i][j] = next_board[i][j]
            # 해당 좌표의 파이어볼이 2개 이상일 경우
            elif length > 1:
                sum_m, sum_s, odd, even = 0, 0, 0, 0  # 질량 합, 속력 합, 홀수 방향 개수, 짝수 방향 개수
                for k in range(length):
                    sum_m += next_board[i][j][k][0]
                    sum_s += next_board[i][j][k][1]
                    if next_board[i][j][k][2] % 2:
                        odd += 1
                    else:
                        even += 1

                # 질량 합을 5로 나눈 몫이 1이상일 경우 방향 조건에 맞게 파이어볼 분열
                if sum_m // 5:
                    # 방향이 전부 홀수이거나 전부 짝수라면, 분열되는 파이어볼의 뱡향을 0, 2, 4, 6으로 저장
                    # 아니라면 1, 3, 5, 7로 저장
                    if odd == length or even == length:
                        board[i][j] = [
                            (sum_m // 5, sum_s // length, 0),
                            (sum_m // 5, sum_s // length, 2),
                            (sum_m // 5, sum_s // length, 4),
                            (sum_m // 5, sum_s // length, 6),
                        ]
                    else:
                        board[i][j] = [
                            (sum_m // 5, sum_s // length, 1),
                            (sum_m // 5, sum_s // length, 3),
                            (sum_m // 5, sum_s // length, 5),
                            (sum_m // 5, sum_s // length, 7),
                        ]

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]  # 파이어볼 이동을 나타낼 3차원 배열

# 8방향 델타(12시부터 시계방향)
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

# 처음 파이어볼 위치를 board에 저장
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r - 1][c - 1].append((m, s, d))  # 질량, 속력, 방향 순서로 tuple 형식으로 저장

# k번 동안 파이어볼 이동 진행
for _ in range(k):
    next_board = move()  # 이동 후 배열
    fireball()  # 파이어볼 이동 후 조치 진행

# 파이어볼 k번 이동 종료 후 남아있는 파이어볼의 질량 합 구하기
ans = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            while board[i][j]:
                m = board[i][j].pop()[0]
                ans += m

print(ans)