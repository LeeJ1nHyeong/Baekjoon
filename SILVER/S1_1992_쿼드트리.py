def divide_and_conquer(x, y, n):
    global ans
    target = board[x][y]  # 타겟 번호 지정

    # 탐색 영역 내에 타겟 번호과 다른 번호가 있다면 4분할로 재탐색
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != target:
                # 출력 형식에 맞게 소괄호 추가
                ans += "("
                divide_and_conquer(x, y, n // 2)  # 왼쪽 위
                divide_and_conquer(x, y + n // 2, n // 2)  # 오른쪽 위
                divide_and_conquer(x + n // 2, y, n // 2)  # 왼쪽 아래
                divide_and_conquer(x + n // 2, y + n // 2, n // 2)  # 오른쪽 아래
                ans += ")"
                return
            
    # 탐색 영역이 모두 같은 번호로 구성되어 있다면 괄호없이 해당 번호를 답에 추가
    ans += target


n = int(input())
board = [list(input()) for _ in range(n)]
ans = ""

divide_and_conquer(0, 0, n)
print(ans)
