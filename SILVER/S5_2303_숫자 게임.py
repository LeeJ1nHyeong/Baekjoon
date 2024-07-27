import itertools

n = int(input())

ans = 0  # 일의 자리 수가 가장 큰 사람의 번호
max_value = 0  # 일의 자리 수 최댓값
for num in range(1, n + 1):
    num_list = list(map(int, input().split()))
    value = 0
    # 5개의 수 중 3개의 수를 골라 일의 자리 수 비교
    for v in itertools.combinations(num_list, 3):
        value = max(value, sum(v) % 10)

    # 일의 자리 수가 최댓값일 경우 바로 최신화
    if value > max_value:
        max_value = value
        ans = num
    # 만약 같다면 번호가 더 큰 사람으로 변경
    elif value == max_value:
        ans = max(ans, num)

# 일의 자리 수가 가장 큰 사람의 번호 출력
print(ans)
