def move_fish():
    next_fish = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if fish[i][j]:
                # 각 물고기별로 진행 가능한 방향을 찾아 이동
                for d in fish[i][j]:
                    is_move = False
                    for k in range(8):
                        ni, nj = i + f_di[(d - k) % 8], j + f_dj[(d - k) % 8]

                        if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                            continue

                        # 진행 방향에 물고기 냄새가 있다면 continue
                        if smell[ni][nj]:
                            continue

                        # 진행 방향에 상어가 있다면 continue
                        if (ni, nj) == (si, sj):
                            continue

                        is_move = True
                        next_fish[ni][nj].append((d - k) % 8)
                        break

                    # 이동이 불가능하다면 그대로 놔두기
                    if not is_move:
                        next_fish[i][j].append(d)

    return next_fish


def delete_smell():
    next_smell = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            # 몬스터 시체가 있는 칸 탐색
            if smell[i][j]:
                smell_ij = []
                # 유지되는 물고기 냄새만 따로 추출하여 next_smell에 저장
                for sm in smell[i][j]:
                    if sm > 1:
                        smell_ij.append(sm - 1)

                next_smell[i][j] = smell_ij

    return next_smell


m, s = map(int, input().split())
fish = [[[] for _ in range(4)] for _ in range(4)]
smell = [[[] for _ in range(4)] for _ in range(4)]

# 물고기 이동 8방향
f_di = [0, -1, -1, -1, 0, 1, 1, 1]
f_dj = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어 이동 4방향
s_di = [-1, 0, 1, 0]
s_dj = [0, -1, 0, 1]

# 물고기 위치와 이동방향 저장
for _ in range(m):
    r, c, d = map(int, input().split())
    fish[r - 1][c - 1].append(d - 1)

# 상어 좌표
si, sj = map(int, input().split())
si -= 1
sj -= 1

for _ in range(s):
    # 물고기 복제
    copy_fish = []

    for i in range(4):
        for j in range(4):
            if fish[i][j]:
                for d in fish[i][j]:
                    copy_fish.append((i, j, d))

    # 물고기 이동
    fish = move_fish()

    # 상어 이동경로 선정
    max_cnt = -1
    max_d1, max_d2, max_d3 = -1, -1, -1

    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                visited = []
                cnt = 0
                ni, nj = si, sj

                # 첫번째 이동
                ni += s_di[d1]
                nj += s_dj[d1]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                visited.append((ni, nj))
                cnt += len(fish[ni][nj])

                # 두번째 이동
                ni += s_di[d2]
                nj += s_dj[d2]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                if (ni, nj) not in visited:
                    cnt += len(fish[ni][nj])
                    visited.append((ni, nj))

                # 세번째 이동
                ni += s_di[d3]
                nj += s_dj[d3]

                if ni < 0 or ni == 4 or nj < 0 or nj == 4:
                    continue

                if (ni, nj) not in visited:
                    cnt += len(fish[ni][nj])
                    visited.append((ni, nj))

                if cnt <= max_cnt:
                    continue

                max_cnt = cnt
                max_d1, max_d2, max_d3 = d1, d2, d3

    ## 상어 이동
    # 첫번째 이동
    si += s_di[max_d1]
    sj += s_dj[max_d1]

    if fish[si][sj]:
        for _ in range(len(fish[si][sj])):
            smell[si][sj].append(3)

        fish[si][sj] = []

    # 두번째 이동
    si += s_di[max_d2]
    sj += s_dj[max_d2]

    if fish[si][sj]:
        for _ in range(len(fish[si][sj])):
            smell[si][sj].append(3)

        fish[si][sj] = []

    # 세번째 이동
    si += s_di[max_d3]
    sj += s_dj[max_d3]

    if fish[si][sj]:
        for _ in range(len(fish[si][sj])):
            smell[si][sj].append(3)

        fish[si][sj] = []

    # 물고기 냄새 제거
    smell = delete_smell()


    # 물고기 복제
    for i, j, d in copy_fish:
        fish[i][j].append(d)

fish_cnt = 0
for i in range(4):
    for j in range(4):
        if fish[i][j]:
            fish_cnt += len(fish[i][j])

print(fish_cnt)
