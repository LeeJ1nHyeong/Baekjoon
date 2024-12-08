n = int(input())

dp_max = [0] * 3
dp_min = [0] * 3

num1, num2, num3 = map(int, input().split())
dp_max[0] = dp_min[0] = num1
dp_max[1] = dp_min[1] = num2
dp_max[2] = dp_min[2] = num3

for i in range(1, n):
    num1, num2, num3 = map(int, input().split())
    dp_max_0, dp_max_1, dp_max_2 = dp_max[0], dp_max[1], dp_max[2]
    dp_min_0, dp_min_1, dp_min_2 = dp_min[0], dp_min[1], dp_min[2]

    dp_max[0] = max(dp_max_0, dp_max_1) + num1
    dp_min[0] = min(dp_min_0, dp_min_1) + num1

    dp_max[1] = max(dp_max_0, dp_max_1, dp_max_2) + num2
    dp_min[1] = min(dp_min_0, dp_min_1, dp_min_2) + num2

    dp_max[2] = max(dp_max_1, dp_max_2) + num3
    dp_min[2] = min(dp_min_1, dp_min_2) + num3

print(max(dp_max), min(dp_min))