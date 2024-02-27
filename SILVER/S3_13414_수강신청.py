import sys
input = sys.stdin.readline

k, l = map(int, input().split())
students = {}  # 수강신청 학번을 저장하기 위한 딕셔너리

for _ in range(l):
    student = input().rstrip()  # 0으로 시작하는 학번도 있기 때문에 문자열로 입력 받기
    
    # students에 학번이 없다면 추가
    if student not in students:
        students[student] = 1
    
    # 학번이 존재한다면 그 학번을 삭제 후 새로 추가
    else:
        del students[student]
        students[student] = 1

students = list(students.keys())  # 학번을 리스트화 시키기

# 학생 수가 수강 가능 인원보다 적다면 모두 출력 
if len(students) < k:
    for s in students:
        print(s)

# 위의 경우를 제외하고 k명 만큼 출력
else:
    for i in range(k):
        print(students[i])