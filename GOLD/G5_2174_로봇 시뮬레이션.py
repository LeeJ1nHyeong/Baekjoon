def simulation():
    for _ in range(m):
        num, command, repeat = input().split()  # 로봇 번호, 명령어, 반복 횟수
        num, repeat = int(num), int(repeat)  # 로봇 번호와 반복 횟수는 int형으로 변환

        i, j, d = robots[num]  # 로봇의 좌표 및 진행 방향 

        # 명령어가 직진(F)일 경우
        if command == "F":
            board[i][j] = 0  # 원래 위치 값 초기화
            # 반복 횟수 만큼 이동
            for _ in range(repeat):
                i, j = i + di[d], j + dj[d]
                # 벽에 충돌할 경우(범위 밖으로 벗어날 경우) 벽 충돌 관련 메세지를 출력 형태에 맞게 return
                if i < 0 or i >= a or j < 0 or j >= b:
                    return f"Robot {num} crashes into the wall"
                # 이동한 좌표에 다른 로봇이 있을 경우 로봇 충돌 관련 메세지를 출력 형태에 맞게 return
                if board[i][j]:
                    return f"Robot {num} crashes into robot {board[i][j]}"
                
            # 명령 실행 종료 후 board에 로봇 저장 후 좌표 최신화
            board[i][j] = num
            robots[num] = [i, j, d]

        # 명령어가 좌우 회전(L, R)일 경우, 반복 횟수 만큼을 d에 더하거나 뺀 다음 4로 나눈 나머지 값을 새로 저장
        elif command == "L":
            d = (d - repeat) % 4
            robots[num][2] = d
        elif command == "R":
            d = (d + repeat) % 4
            robots[num][2] = d

    return "OK"  # 모든 명령이 실행됐을 경우 이상이 없다는 뜻이므로 "OK" return


a, b = map(int, input().split())
n, m = map(int, input().split())
# 로봇 이동 시뮬레이션을 위한 2차원 리스트, 편의를 위해 시계방향 90도 돌린 형태로 생성
board = [[0] * b for _ in range(a)]

# 4방향 델타 탐색을 위한 리스트 (NESW 순서)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

robots = [[]]  # 각 로봇 별 좌표와 방향을 담을 2차원 리스트

# 로봇 좌표 및 방향을 리스트에 추가
for num in range(1, n + 1):
    x, y, d = input().split()
    x, y = int(x) - 1, int(y) - 1
    board[x][y] = num  # 각 로봇의 위치를 board에 저장

    # N - 0, E - 1, S - 2, W - 3으로 숫자로 변환하여 robots에 추가
    tmp = [x, y]
    if d == "E":
        tmp.append(1)
    elif d == "S":
        tmp.append(2)
    elif d == "W":
        tmp.append(3)
    elif d == "N":
        tmp.append(0)

    robots.append(tmp)

print(simulation())  # 시뮬레이션 진행
