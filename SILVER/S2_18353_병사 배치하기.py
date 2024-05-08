n = int(input())
ability = list(map(int, input().split()))
dp = [1] * n

# 1번부터 n번까지의 병사를 순회하면서 dp 진행
for i in range(1, n):
    for j in range(i):
        if ability[i] < ability[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))