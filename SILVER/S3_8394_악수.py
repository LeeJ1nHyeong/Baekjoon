# 전형적인 피보나치 수열

# 풀이 1 - dp 배열 활용
n = int(input())
dp = [0] * (n + 1)

if n == 1:
    print(1)
    
elif n == 2:
    print(2)

else:
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 10  # 문제 조건에 맞게 마지막 자리를 저장

    print(dp[n])


# 풀이 2 - 변수 2개 활용
n = int(input())
a, b = 1, 2

for i in range(1, n):
    a, b = b, (a + b) % 10

print(a)