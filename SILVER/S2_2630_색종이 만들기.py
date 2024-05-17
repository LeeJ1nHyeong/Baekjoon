def divide_and_conquer(x, y, n):
    global white, blue
    target = paper[x][y]  # 타겟 번호
    divide = n // 2

    # 탐색 영역 내에 target과 다른 번호가 있다면 4분할 후 재탐색
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != target:
                divide_and_conquer(x, y, divide)
                divide_and_conquer(x, y + divide, divide)
                divide_and_conquer(x + divide, y, divide)
                divide_and_conquer(x + divide, y + divide, divide)

                return
            
    # 각 번호에 해당하는 색깔에 1 추가
    if target == 0:
        white += 1
    else:
        blue += 1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0  # 하얀색 종이, 파란색 종이 개수

divide_and_conquer(0, 0, n)  # 분할정복 진행

# 하얀색, 파란색 종이 개수 출력
print(white)
print(blue)
