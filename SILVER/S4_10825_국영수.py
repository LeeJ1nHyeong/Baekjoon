n = int(input())
grade = []

# 이름, 국어 성적, 영어 성적, 수학 성적을 튜플 형태로 리스트에 저장
for _ in range(n):
    name, korean, english, math = input().split()
    grade.append((name, int(korean), int(english), int(math)))

# 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순으로 정렬
grade.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 정렬 후 이름 출력
for g in grade:
    print(g[0])