n = int(input())
num_list = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1  # 처음 값을 1로 설정

# 처음부터 i번 인덱스까지 범위를 설정해 dp를 활용하여 탐색
for i in range(n):
    for j in range(i):
        # 현재 인덱스가 더 작은 값일 경우 비교 인덱스의 dp값에 1을 더한 값과 현재 인덱스의 dp값 중 더 높은 값을 선택
        if num_list[i] < num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

        # 현재 인덱스가 더 크거나 같은 값일 경우 최솟값을 1로 정해놓고 현재 dp값과 비교
        else:
            dp[i] = max(dp[i], 1)

print(max(dp))  # dp의 최댓값 출력