n, k = map(int, input().split())
coin_list = []  # 동전의 종류를 담을 리스트
for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_list.sort()  # 동전 오름차순

dp = [0] + [10001] * k  # 최솟값을 지정하기 위해 10001로 채운 dp 리스트

# dp 진행
for i in range(1, k + 1):
    for coin in coin_list:
        if i < coin:
            break
        else:
            dp[i] = min(dp[i - coin] + 1, dp[i])

print(dp[k] if dp[k] != 10001 else -1)  # dp[k]값이 10001이라면 -1로 출력