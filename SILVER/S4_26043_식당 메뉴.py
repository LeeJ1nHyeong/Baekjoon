from collections import deque
import sys
input = sys.stdin.readline

# 정답 출력
def answer(lst):
    # 리스트에 학생이 있으면 오름차순 후 출력
    if lst:
        lst.sort()
        print(*lst)
        return

    print("None")  # 없으면 None 출력


n = int(input())
queue = deque()  # 식당 입구 대기 목록

student_a = []  # 학생 목록 A
student_b = []  # 학생 목록 B
student_c = []  # 학생 목록 C

for _ in range(n):
    command, *s = map(int, input().split())

    # 유형 1
    if command == 1:
        # 학생 번호 a, 좋아하는 메뉴 번호 b를 튜플 형태로 queue에 저장
        a, b = s
        queue.append((a, b))

    # 유형 2
    else:
        # 메뉴 번호 b
        b = s[0]

        # 대기 줄 가장 앞의 학생이 식사
        student, food = queue.popleft()

        # 좋아하는 메뉴라면 A, 싫어하는 메뉴라면 B에 추가
        if b == food:
            student_a.append(student)
        else:
            student_b.append(student)

# 모든 정보 처리 후 대기 줄에 학생이 있다면 C에 추가
if queue:
    while queue:
        student, food = queue.popleft()
        student_c.append(student)

# 학생 목록 출력
answer(student_a)
answer(student_b)
answer(student_c)
