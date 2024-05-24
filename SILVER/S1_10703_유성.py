r, c = map(int, input().split())
sky = [list(input()) for _ in range(r)]

min_move = r  # 유성이 이동할 수 있는 최솟값

for j in range(c):
    max_meteor, min_ground = -1, r  # 유성의 최대 i 좌표, 땅의 최소 i 좌표
    for i in range(r):
        # 유성의 최대 i 좌표 탐색
        if sky[i][j] == "X":
            max_meteor = max(max_meteor, i)
        # 땅의 최소 i 좌표 탐색
        elif sky[i][j] == "#":
            min_ground = min(min_ground, i)

        # 유성 최대 i 좌표에 변화가 있을 경우 이동 최솟값 여부 확인
        if max_meteor != -1:
            min_move = min(min_ground - max_meteor - 1, min_move)

# 유성 이동
for i in range(r - 1, -1, -1):
    for j in range(c):
        if sky[i][j] == "X":
            sky[i][j], sky[i + min_move][j] = ".", "X"

# 형식에 맞게 출력
for s in sky:
    print("".join(s))
