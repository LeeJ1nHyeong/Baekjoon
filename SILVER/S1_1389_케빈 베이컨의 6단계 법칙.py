n, m = map(int, input().split())
board = [[1e9] * n for _ in range(n)]  # 몇 단계를 거쳐서 친구인지 저장

# 친구 관계를 양방향으로 저장
for _ in range(m):
    s, e = map(int, input().split())

    board[s - 1][e - 1] = 1
    board[e - 1][s - 1] = 1

# 같은 인덱스는 0으로 변경
for i in range(n):
    board[i][i] = 0

# i에서 j 사이의 단계와 중간에 k를 거쳤을 때의 단계 중 최솟값을 저장
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

min_cnt, min_num = 1e9, 0  # 케빈 베이컨 최솟값과 친구 번호

# 케빈 베이컨 최솟값을 갖는 번호 탐색
for i in range(n):
    if sum(board[i]) < min_cnt:
        min_cnt = sum(board[i])
        min_num = i + 1

print(min_num)  # 최솟값을 갖는 번호 출력
