n = int(input())
box = list(map(int, input().split()))
dp = [0] * n

# 처음부터 i번째 값을 비교하여 i번째 값이 더 클 경우 dp 값을 1 추가하는 방식으로 저장
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # dp 최댓값 출력
