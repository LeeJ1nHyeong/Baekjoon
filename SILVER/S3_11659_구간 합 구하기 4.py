import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [0] * (n + 1)

# 처음부터 i + 1번째 숫자(i번 인덱스)까지의 합을 dp에 저장
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + numbers[i - 1]

# dp를 활용하여 답 출력
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[e] - dp[s - 1])