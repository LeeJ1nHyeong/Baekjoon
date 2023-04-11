bingo = [list(map(int, input().split())) for _ in range(5)]

num_list = []
for _ in range(5):
    lst = list(map(int, input().split()))
    for i in range(5):
        num_list.append(lst[i])

bingo_cnt = 0

row = [0] * 5
column = [0] * 5
cross = [0] * 2

for n in range(25):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num_list[n]:
                row[i] += 1
                column[j] += 1

                if i == j:
                    cross[0] += 1

                if i + j == 4:
                    cross[1] += 1
                break

    for i in range(5):
        if row[i] == 5:
            bingo_cnt += 1
            row[i] = 0

        if column[i] == 5:
            bingo_cnt += 1
            column[i] = 0

    for i in range(2):
        if cross[i] == 5:
            bingo_cnt += 1
            cross[i] = 0

    if bingo_cnt >= 3:
        print(n+1)
        break