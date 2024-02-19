n = int(input())
boxes = list(map(int, input().split()))
dp = [0] * n

# 1번 상자(0번 인덱스)부터 i번 상자(i - 1번 인덱스)까지 순회하면서 dp 진행
for i in range(n):
    for j in range(i):
        if boxes[i] > boxes[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))