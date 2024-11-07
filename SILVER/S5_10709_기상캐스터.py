n, m = map(int, input().split())
sky = [list(input()) for _ in range(n)]
weather = [[-1] * m for _ in range(n)]

for i in range(n):
    isCloud = False  # 탐색 행에 구름이 있는지 체크하는 flag

    # 각 행별로 구름이 있는지 탐색
    for j in range(m):
        # 탐색 칸이 구름일 경우 whether 칸을 0으로 저장 후 flag를 True로 변경
        if sky[i][j] == "c":
            weather[i][j] = 0
            isCloud = True

        # 탐색 칸이 구름이 아닐 경우
        else:
            # 탐색 행에 구름이 존재한다면 whether의 이전 칸에 1을 더한 값을 현재 칸에 저장
            if isCloud:
                weather[i][j] = weather[i][j - 1] + 1

# 형식에 맞게 출력
for w in weather:
    print(*w)
