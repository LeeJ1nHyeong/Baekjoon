'''
1. 시작 좌표(7, 0)부터 8방향 및 원래 위치를 탐색하여 이동 가능한 좌표 탐색(character_move 함수 실행)
2-1. 이동할 수 있는 좌표가 없을 경우 바로 0을 return하여 bfs 종료
2-2. 이동 가능한 좌표가 존재할 경우 벽 이동 진행 (wall_move() 함수 실행)
3. for문 8회 진행이 완료가 된다면, 탈출이 가능하다는 뜻이므로 1 return
'''

from collections import deque

# bfs
def bfs():
    queue = deque()
    queue.append((7, 0))  # 시작점 (7, 0)을 queue에 추가

    # board는 8 X 8 고정이기 때문에 최대 8번만 수행하면 되므로 for문 8번 실행
    for _ in range(8):
        move_list = character_move(queue)  # 캐릭터 이동이 가능한 좌표들을 담은 리스트

        # 이동 가능한 좌표가 없다면 0 return
        if not move_list:
            return 0

        wall_move()  # 벽 이동

        queue = deque(move_list)  # 다음 탐색을 위해 queue를 이동 후 좌표 리스트로 최신화

    return 1  # 8번의 for문 수행완료 == 탈출 가능이므로 1 return

# 캐릭터 이동
def character_move(lst):
    temp = []  # 이동 후 좌표를 담을 리스트
    while lst:
        i, j = lst.popleft()
        # 8방향과 제자리 좌표를 탐색하여 board 내에서 이동 가능한 지 확인
        for di, dj in (0, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < 8 and 0 <= nj < 8 and board[ni][nj] == ".":
                # 이동한 좌표가 가장 위 또는 이동한 좌표의 바로 위가 벽이 아니라면 temp에 좌표 추가
                if (ni == 0 or board[ni - 1][nj] != "#") and (ni, nj) not in temp:
                    temp.append((ni, nj))

    return temp  # while문 종료 후 이동 가능한 좌표 리스트 return

# 벽 이동
def wall_move():
    # 가장 밑부터 위로 탐색하면서 벽 이동 진행
    for i in range(7, 0, -1):
        for j in range(8):
            if board[i - 1][j] == "#":
                board[i][j] = "#"
            else:
                board[i][j] = "."


board = [list(input()) for _ in range(8)]
print(bfs())
