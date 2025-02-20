n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n

# 최장 증가 부분 수열 길이를 dp로 저장
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 마지막 인덱스부터 거꾸로 탐색하여 최장 증가 부분 수열 찾기
partial = []
now = max(dp)
for i in range(n - 1, -1, -1):
    if not now:
        break

    if dp[i] == now:
        partial.append(numbers[i])
        now -= 1

partial.reverse()
print(max(dp))
print(*partial)
