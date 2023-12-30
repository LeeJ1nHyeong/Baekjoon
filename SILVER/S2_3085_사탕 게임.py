'''
1. board 가로줄 및 세로줄을 탐색하면서 인접한 부분의 색깔이 다른 부분 찾기
2. 색깔이 다른 인접한 두 사탕의 위치를 교환
3. 교환 후 가로줄 및 세로줄 탐색하면서 같은 색으로 이루어진 가장 긴 연속 부분을 찾기 (eat 함수 실행)
4. 최대값 출력
'''

def eat():  # 가장 긴 연속부분 찾기
    global max_cnt

    for i in range(n):  # 가로줄 탐색
        cnt = 1
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
            else:
                cnt = 1

            max_cnt = max(cnt, max_cnt)

    for i in range(n):  # 세로줄 탐색
        cnt = 1
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                cnt += 1
            else:
                cnt = 1

            max_cnt = max(cnt, max_cnt)


n = int(input())
board = [list(map(str, input())) for _ in range(n)]
max_cnt = 1

# 가로줄 탐색
for i in range(n):
    for j in range(n - 1):
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            eat()
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

# 세로줄 탐색
for i in range(n):
    for j in range(n - 1):
        if board[j][i] != board[j + 1][i]:
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
            eat()
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]

print(max_cnt)