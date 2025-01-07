t = int(input())

for num in range(1, t + 1):
    board = [list(map(int, input().split())) for _ in range(9)]

    check = True

    # 가로줄 탐색
    for row in board:
        if len(set(row)) != 9:
            check = False
            break

    # 세로줄 탐색
    if check:
        for column in zip(*board):
            if len(set(column)) != 9:
                check = False
                break

    # 3X3 탐색
    if check:
        for i in range(3):
            for j in range(3):
                square = [board[3 * i + r][3 * j + c] for r in range(3) for c in range(3)]
                if len(set(square)) != 9:
                    check = False
                    break

    ans = "CORRECT" if check else "INCORRECT"
    print(f"Case {num}: {ans}")

    # 개행 처리
    try:
        input()

    except EOFError:
        break
