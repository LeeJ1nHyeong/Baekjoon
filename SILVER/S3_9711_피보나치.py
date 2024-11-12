t = int(input())

fibonacci = [0] * 10001
fibonacci[1] = 1

# dp를 활용하여 피보나치 수를 미리 계산하여 저장
for i in range(2, 10001):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

# 각 테스트케이스 별로 p번째 피보나치 수를 q로 나눈 값을 계산 후 출력
for tc in range(1, t + 1):
    p, q = map(int, input().split())

    m = fibonacci[p] % q

    print(f"Case #{tc}: {m}")
