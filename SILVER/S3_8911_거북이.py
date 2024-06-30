t = int(input())

for _ in range(t):
    command = input()  # 명령 목록

    max_i, min_i = 0, 0  # 최대 i값, 최소 i값
    max_j, min_j = 0, 0  # 최대 j값, 최소 j값

    i, j = 0, 0  # 현재 좌표

    # 상우하좌 순서
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    d = 0  # 방향

    # 명령에 따른 행동 진행
    for c in command:
        # 전진
        if c == "F":
            i += di[d]
            j += dj[d]

            # 이동 후 좌표의 최대, 최소 여부 확인
            max_i = max(i, max_i)
            min_i = min(i, min_i)
            max_j = max(j, max_j)
            min_j = min(j, min_j)
        
        # 후진
        elif c == "B":
            i -= di[d]
            j -= dj[d]

            # 이동 후 좌표의 최대, 최소 여부 확인
            max_i = max(i, max_i)
            min_i = min(i, min_i)
            max_j = max(j, max_j)
            min_j = min(j, min_j)

        # 왼쪽 회전
        elif c == "L":
            d = (d - 1) % 4

        # 오른쪽 회전
        elif c == "R":
            d = (d + 1) % 4

    # 직사각형 범위의 넓이 출력
    ans = (max_i - min_i) * (max_j - min_j)
    print(ans)
