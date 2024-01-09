'''
1. 뱀이 존재하는 좌표를 담을 덱(snake)과 방향 전환 정보를 담을 덱(turn)을 생성
2. 1초씩 증가시킨 후 뱀의 머리에 해당하는 좌표에서 진행방향으로 한칸 이동한 좌표를 덱의 가장 앞에 추가
3. 뱀의 머리 좌표(head_i, head_j)가 벽에 부딪히거나 snake 덱에 존재하면 while문 종료
4. 뱀의 머리 좌표에 사과가 있는지 탐색 (apple 함수 실행)
    4-1. 사과가 있다면 보드의 해당 좌표를 0으로 바꿈
    4-2. 사과가 없다면 뱀의 꼬리좌표를 pop
5. 현재 시간이 turn 덱에 존재한다면 방향에 따라 인덱스(idx) 변환 후 해당 정보 pop (popleft)
'''

def apple(i, j):  # 보드 내 사과 탐색
    if board[i][j] != 1:
        snake.pop()
    else:
        board[i][j] = 0
        
def rotate():  # 방향 전환
    global idx
    
    if not turn:  # turn 덱에 아무 것도 없을 경우
        return
    
    # 해당 시간이 turn 덱에 존재할 경우 방향 전환 진행
    if second == int(turn[0][0]):
        if turn[0][1] == "L":
            idx = (idx - 1) % 4
        elif turn[0][1] == "D":
            idx = (idx + 1) % 4
        turn.popleft()  # 방향 전환 후 해당 정보 pop

from collections import deque

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]  # 보드
snake = deque([(0, 0)])  # 뱀 좌표를 담을 덱

second = 0  # 진행 시간
idx = 0  # 방향 전환 인덱스

# 3, 6, 9, 12시 방향 순서
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 사과
k = int(input())

for _ in range(k):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1

# 방향 전환
l = int(input())
turn = deque()

for _ in range(l):
    turn_sec, direction = input().split()
    turn.append((turn_sec, direction))

# 게임 진행
while True:
    second += 1  # 시간 1초씩 증가
    snake.appendleft((snake[0][0] + di[idx], snake[0][1] + dj[idx]))  # 뱀 머리 이동
    head_i, head_j = snake.popleft()

    # 뱀 머리가 벽에 부딪히거나 뱀 몸통에 부딪히면 while문 종료
    if head_i < 0 or head_i >= n or head_j < 0  or head_j >= n or (head_i, head_j) in snake:
        break

    snake.appendleft((head_i, head_j))  # pop시킨 뱀 머리 좌표 다시 원위치
    
    apple(head_i, head_j)  # 사과 탐색
    
    rotate()  # 방향 전환 여부 탐색

print(second)