# 상어 정보
class Shark:
    def __init__(self, num, i, j, s, d, z):
        self.num = num  # 상어 번호
        self.i = i  # 상어 i좌표
        self.j = j  # 상어 j좌표
        self.s = s  # 상어 속력
        self.d = d  # 상어 이동 방향
        self.z = z  # 상어 크기

    # 상어 이동
    def move(self):
        # 속력을 한바퀴(상하 == (r - 1) * 2, 좌우 == (c - 1) * 2)로 나눈 값 만큼 이동을 진행
        # 상하
        if self.d == 0 or self.d == 1:
            cycle = (r - 1) * 2
            move = self.s % cycle
            for _ in range(move):
                # 끝에 도달하면 방향 전환
                if self.i == 0:
                    self.d = 1
                elif self.i == r - 1:
                    self.d = 0
                self.i += di[self.d]
        # 좌우
        else:
            cycle = (c - 1) * 2
            move = self.s % cycle
            for _ in range(move):
                # 끝에 도달하면 방향 전환
                if self.j == 0:
                    self.d = 2
                elif self.j == c - 1:
                    self.d = 3
                self.j += dj[self.d]

    # 상어 사망
    def dead(self):
        is_alive[self.num] = 0

# board 초기화
def init():
    for i in range(r):
        for j in range(c):
            board[i][j] = -1


r, c, m = map(int, input().split())
board = [[-1] * c for _ in range(r)]

# 상하우좌
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

sharks = []  # 상어 정보를 담을 리스트
is_alive = [1] * m  # 상어 생존 여부

# 잡은 상어 크기의 합
ans = 0
for num in range(m):
    i, j, s, d, z = map(int, input().split())
    # 상어 클래스 생성 후 정보를 sharks에 저장
    sharks.append(Shark(num, i - 1, j - 1, s, d - 1, z))

for j in range(c):
    # 상어를 board에 표시
    init()
    for shark in sharks:
        num = shark.num
        si, sj = shark.i, shark.j

        if not is_alive[num]:
            continue
        board[si][sj] = num

    # 낚시왕이 있는 열에 있는 상어 중 가장 가까운 상어 잡기
    for i in range(r):
        if board[i][j] != -1:
            ans += sharks[board[i][j]].z
            sharks[board[i][j]].dead()
            break

    # 상어 이동
    for shark in sharks:
        num = shark.num
        if not is_alive[num]:
            continue

        shark.move()

    # 이동 후 board 최신화
    init()
    for shark in sharks:
        num = shark.num
        si, sj = shark.i, shark.j

        # 사망한 상어는 제외
        if not is_alive[num]:
            continue

        if board[si][sj] == -1:
            board[si][sj] = num

        # 해당 칸에 다른 상어가 있을 경우 크기 비교 후 더 큰 상어가 생존
        else:
            if sharks[board[si][sj]].z > shark.z:
                shark.dead()
            else:
                sharks[board[si][sj]].dead()
                board[si][sj] = num

# 낚시왕이 잡은 상어 크기의 합 출력
print(ans)
