n = int(input())
user = []

# 회원의 나이와 이름, 가입순서를 튜플 형태로 저장
for num in range(1, n + 1):
    age, name = input().split()
    user.append((int(age), num, name))

# 나이 오름차순, 나이가 같을 경우 가입 순서대로 정렬
user.sort(key=lambda x: (x[0], x[1]))

# 정렬된 리스트에서 나이와 이름을 출력
for age, num, name in user:
    print(age, name)
