n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

# 처음 값을 최솟값으로 시작
min_num = a[0]

for i in range(1, n):
    # 숫자를 추가하면서 최솟값 여부 확인
    min_num = min(min_num, a[i])
    # 이전 dp값과 현재값에서 최솟값을 뺀 값 중 최댓값을 dp에 저장
    dp[i] = max(dp[i - 1], a[i] - min_num)

print(*dp)  # dp 출력