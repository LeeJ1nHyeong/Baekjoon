N = int(input())

room = [list(map(str,input())) for _ in range(N)]

sleep_row = 0
sleep_column = 0

for i in range(N):
    cnt_row = 0
    cnt_column = 0
    for j in range(N):
        # 가로줄 탐색
        if room[i][j] == '.':
            cnt_row += 1
        else:
            if cnt_row >= 2:
                sleep_row += 1
                cnt_row = 0
            else:
                cnt_row = 0

        # 세로줄 탐색
        if room[j][i] == '.':
            cnt_column += 1
        else:
            if cnt_column >= 2:
                sleep_column += 1
                cnt_column = 0
            else:
                cnt_column = 0

    if cnt_row >= 2:
        sleep_row += 1
    if cnt_column >= 2:
        sleep_column += 1

print(sleep_row, sleep_column)