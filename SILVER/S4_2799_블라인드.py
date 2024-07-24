n, m = map(int, input().split())
blind = [list(input()) for _ in range(5 * n + 1)]
blind_type = [0] * 5  # 창문 형태

# 각 창문 칸의 왼쪽 위부터 탐색
for i in range(n):
    for j in range(m):
        cnt = 0
        si, sj = 5 * i + 1, 5 * j + 1
        # 창문 윗줄부터 아래로 탐색하여 블라인드가 끝나는 지점 탐색
        while cnt != 4:
            if blind[si][sj] == ".":
                break
            si += 1
            cnt += 1

        # 탐색 후 해당 유형에 1 추가
        blind_type[cnt] += 1

# 창문 형태 유형별 개수 출력
print(*blind_type)
