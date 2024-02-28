n = int(input())
num_list = list(map(int, input().split()))
dp = [0] * n  # dp

for i in range(n):
    dp[i] += num_list[i]
    # i번 인덱스까지 숫자 비교 후 조건에 맞게 더하기
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + num_list[i])
        else:
            dp[i] = max(dp[i], num_list[i])

print(max(dp))  # 최댓값 출력