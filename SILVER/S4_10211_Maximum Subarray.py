t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [0] * (n + 1)
    ans = -1e9

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + numbers[i - 1]

    for i in range(n):
        for j in range(i + 1, n + 1):
            subarray = dp[j] - dp[i]
            ans = max(ans, subarray)

    print(ans)
