# 투 포인터를 이용한 풀이

n, m = map(int, input().split())
num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)

num_list.sort()  # 오름차순 정렬

min_diff = 2 * 10e9  # 문제 조건 상 나올 수 있는 최소 차이의 최댓값

i, j = 0, 0  # 같은 수를 고를 수 있기 때문에 시작 인덱스를 둘 다 0으로 설정

while i < n and j < n:
    diff = abs(num_list[i] - num_list[j])
    if diff == m:  # 두 수의 차이가 m이 나오면 while문 종료
        min_diff = m
        break
    elif diff > m:
        min_diff = min(diff, min_diff)
        i += 1
    elif diff < m:
        j += 1

print(min_diff)