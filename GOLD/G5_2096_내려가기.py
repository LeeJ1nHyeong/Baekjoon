n = int(input())

# 최댓값, 최솟값을 담을 길이 3 리스트를 2개 생성(메모리 제한)
dp_max = [0] * 3
dp_min = [0] * 3

# 처음 값을 최댓값 dp, 최솟값 dp에 각각 저장
num1, num2, num3 = map(int, input().split())
dp_max[0] = dp_min[0] = num1
dp_max[1] = dp_min[1] = num2
dp_max[2] = dp_min[2] = num3

for i in range(1, n):
    num1, num2, num3 = map(int, input().split())
    # 이전 값들을 새로운 변수에 저장
    dp_max_0, dp_max_1, dp_max_2 = dp_max[0], dp_max[1], dp_max[2]
    dp_min_0, dp_min_1, dp_min_2 = dp_min[0], dp_min[1], dp_min[2]

    # 문제 조건에 맞게 정해진 이전 값에 현재 위치의 값을 더하여 저장
    dp_max[0] = max(dp_max_0, dp_max_1) + num1
    dp_min[0] = min(dp_min_0, dp_min_1) + num1

    dp_max[1] = max(dp_max_0, dp_max_1, dp_max_2) + num2
    dp_min[1] = min(dp_min_0, dp_min_1, dp_min_2) + num2

    dp_max[2] = max(dp_max_1, dp_max_2) + num3
    dp_min[2] = min(dp_min_1, dp_min_2) + num3

print(max(dp_max), min(dp_min))