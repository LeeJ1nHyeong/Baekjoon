n = int(input())
num = list(map(int, input().split()))

# 숫자의 집합을 정렬한 리스트
num_set = sorted(list(set(num)))

# 정렬된 집합에 있는 숫자를 key로, 오름차순 순서를 value로 하는 딕셔너리 생성
num_dict = {num_set[i] : i for i in range(len(num_set))}

# 수직선 내에 중복 없이 더 높은 좌표의 개수 출력
for i in range(n):
    print(num_dict[num[i]], end=" ")
    