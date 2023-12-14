'''
1. 컨베이어 벨트 윗 부분 리스트(upper_belt), 로봇 존재 여부 리스트(robot) 만들기
2. 각 단계별로 컨베이어 벨트 리스트에 -1을 하여 회전 (rotate 함수 실행)
    2-1. 이 때 컨베이어 벨트 윗부분 끝에 로봇이 도달하면 로봇 제거 (get_off 함수 실행)
3. 벨트에 올린 순서대로 조건에 따라 로봇 이동(move 함수 실행)
    3-1. 이동하려는 칸에 로봇이 없고 내구도가 0이 아니라면 회전방향으로 로봇 이동, 그렇지 않다면 가만히 있기
    3-2. 이 때 컨베이어 벨트 윗부분 끝에 로봇이 도달하면 로봇 제거 (get_off 함수 실행)
4. 컨베이어 벨트 첫 부분의 내구도가 0이 아니라면 로봇 올리기(get_on 함수 실행)
5. 위 cycle 진행 후 내구도 0인 부분이 k개 이상이면 과정 종료, 아니라면 cycle 반복
'''

def rotate():  # 컨베이어 벨트 회전
    global upper_belt

    for i in range(n):
        upper_belt[i] -= 1
        if upper_belt[i] == -1:  # 인덱스가 -1이라면 가장 높은 인덱스(2n - 1)로 치환
            upper_belt[i] = 2 * n - 1

    get_off()  # 회전 후에 로봇이 컨베이어 벨트 윗부분 끝에 도달하면 로봇 제거

    return

def move():  # 로봇 이동
    global upper_belt

    # 먼저 올린 로봇부터 진행하기 위해 upper_belt 배열 뒤집기
    reverse_upper_belt = upper_belt[::-1]
    for i in range(n):
        now_index = reverse_upper_belt[i]
        next_index = (now_index + 1) % (2 * n)
        # 현재 위치에 로봇이 있을 때, 다음 위치에 로봇이 없고 내구도가 0이 아니라면 로봇 이동
        if robot[now_index]:
            if not robot[next_index] and belt[next_index]:
                robot[next_index] += 1
                robot[now_index] -= 1
                belt[next_index] -= 1

    get_off()  # 로봇 이동 후 컨베이어 벨트 윗부분 끝에 도달하면 로봇 제거

    return

def get_off():  # 로봇 제거
    global upper_belt

    # 로봇이 컨베이어 벨트 윗부분 끝에 도달하면 로봇 제거
    if robot[upper_belt[-1]]:
        robot[upper_belt[-1]] -= 1

    return

def get_on():  # 로봇 올리기
    global upper_belt

    # 컨베이어 벨트 첫부분의 내구도가 0이 아니라면 로봇 올리기
    if belt[upper_belt[0]]:
        robot[upper_belt[0]] = 1
        belt[upper_belt[0]] -= 1

    return

n, k = map(int, input().split())
belt = list(map(int, input().split()))
upper_belt = []  # 컨베이어 벨트 윗 부분
robot = [0 for _ in range(2 * n)]  # 로봇 존재 여부
stage = 0  # 단계

for i in range(n):
    upper_belt.append(i)

while True:
    stage += 1  # 단계 증가
    rotate()
    move()
    get_on()
    if belt.count(0) >= k:  # 내구도 0인 부분이 k개 이상이면 과정 종료
        break

print(stage)