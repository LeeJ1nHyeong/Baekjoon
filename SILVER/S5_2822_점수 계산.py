scores = []

# 점수와 문제 번호를 튜플 형태로 저장
for num in range(1, 9):
    score = int(input())
    scores.append((score, num))

# 점수 내림차순으로 정렬
scores.sort(reverse=True)

sum_score = 0
num_list = []
# 상위 5개의 퀴즈 점수를 더하고 문제 번호를 리스트에 추가
for score, num in scores[:5]:
    sum_score += score
    num_list.append(num)

# 문제 번호 오름차순 정렬
num_list.sort()

# 점수 합과 문제 번호 출력
print(sum_score)
print(*num_list)
