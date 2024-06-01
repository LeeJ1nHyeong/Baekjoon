t = int(input())
k = int(input())
coin = []  # 동전을 담을 리스트

# 동전 금액과 개수를 튜플 형태로 리스트에 추가
for _ in range(k):
    coin.append(tuple(map(int, input().split())))

dp = [0] * (t + 1)  # 0원부터 t원까지의 dp
dp[0] = 1  # 아무것도 없을 때 0원이므로 dp[0] = 1

for p, n in coin:
    # t원부터 역순으로 탐색
    for i in range(t, 0, -1):
        # 현재 금액에서 0원 미만이 되지 않는 동전 조합에 대해 dp값 추가
        for j in range(1, n + 1):
            if i - p * j >= 0:
                dp[i] += dp[i - p * j]

print(dp[t])  # t원을 만들 수 있는 경우의 수 출력
