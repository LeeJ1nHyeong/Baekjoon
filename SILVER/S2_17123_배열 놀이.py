t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    row_sum = [0] * n  # 각 행의 합
    column_sum = [0] * n  # 각 열의 합

    # 처음 각 행의 합과 각 열의 합 저장
    for i in range(n):
        row_sum[i] = sum(board[i])
        column_sum[i] = sum([board[j][i] for j in range(n)])

    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())

        # 각 범위에 더해지는 v값 만큼 행의 합과 열의 합에 적용
        for i in range(r1 - 1, r2):
            row_sum[i] += (c2 - c1 + 1) * v

        for i in range(c1 - 1, c2):
            column_sum[i] += (r2 - r1 + 1) * v

    # 행의 합과 열의 합 출력
    print(*row_sum)
    print(*column_sum)
