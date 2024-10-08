n = int(input())
student = [tuple(input().split()) for _ in range(n)]

# 각 학생의 생년월일 오름차순 정렬
student.sort(key=lambda x: (x[3], int(x[2]), int(x[1])))

# 나이가 가장 적은 사람과 가장 많은 사람 출력
print(student[-1][0])
print(student[0][0])
