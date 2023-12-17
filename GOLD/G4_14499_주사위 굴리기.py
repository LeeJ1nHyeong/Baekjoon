'''
1. 주사위를 나타내기 위한 리스트(dice) 및 동, 서, 북, 남 순서로 델타 리스트(dx, dy) 생성
2. 주사위 전개도 모양을 고정한 상태에서 이동방향(command)에 따른 전개도 형태 생성(rotate 함수)
3. 이동방향 좌표 이동 후(nx, ny) 이 좌표가 이동 가능한 지 판별
4. 이동 가능한 경우 rotate 함수 실행 후 해당 좌표의 board 값에 따라 진행
    4-1. board 값이 0일 경우, 주사위 바닥면 값(dice[5])을 복사함
    4-2. board 값이 0이 아닐 경우, 주사위 바닥면 값을 board값으로 복사 후 board값 0으로 교체
'''

def rotate(d):  # 주사위 회전
    if d == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif d == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif d == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dice = [0] * 6  # 주사위

# 동, 서, 북, 남 순서(편의를 위해 4+1개로 리스트 제작)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for command in commands:
    nx, ny = x + dx[command], y + dy[command]  # 이동 명령 실행 시의 좌표
    # 이동 후 좌표가 이동 가능한 경우 행동 실행
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        rotate(command)
        if not board[x][y]:  # board 값이 0일 경우 주사위 바닥면을 복사
            board[x][y] = dice[5]
        else:  # board 값이 0이 아닌 경우 주사위 바닥면을 board값으로 교체하고 board값은 0으로 교체
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])