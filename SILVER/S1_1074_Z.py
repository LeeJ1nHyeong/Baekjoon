def divide_and_conquer(n, r, c):
    # n이 1일 경우 좌표에 해당하는 값을 return
    if n == 1:
        return 2 * r + c
    
    ## 각 좌표의 위치에 따라 해당하는 값을 return
    # 2사분면
    if r < 2 ** (n - 1) and c < 2 ** (n - 1):
        return divide_and_conquer(n - 1, r, c)
    # 1사분면
    elif r < 2 ** (n - 1) <= c:
        return 2 ** (2 * n - 2) + divide_and_conquer(n - 1, r, c - 2 ** (n - 1))
    # 3사분면
    elif r >= 2 ** (n - 1) > c:
        return 2 ** (2 * n - 1) + divide_and_conquer(n - 1, r - 2 ** (n - 1), c)
    # 4사분면
    else:
        return 3 * 2 ** (2 * n - 2) + divide_and_conquer(n - 1, r - 2 ** (n - 1), c - 2 ** (n - 1))


n, r, c = map(int, input().split())

print(divide_and_conquer(n, r, c))  # 분할정복 진행
