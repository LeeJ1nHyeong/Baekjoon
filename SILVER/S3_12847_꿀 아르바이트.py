n, m = map(int, input().split())
salary = list(map(int, input().split()))
dp = [0] * (n + 1)  # 누적 합

# 누적 합 저장
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + salary[i - 1]

ans = 0
s, e = 0, m  # 슬라이딩 윈도우 투 포인터

# 거리가 m인 투 포인터를 한 칸씩 이동하면서 최댓값 탐색
while e <= n:
    ans = max(ans, dp[e] - dp[s])

    s += 1
    e += 1

# 최댓값 출력
print(ans)
