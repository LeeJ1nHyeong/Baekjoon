n = int(input())
numbers = list(input().split())

# 버블 정렬 활용
for i in range(n - 1, 0, -1):
    for j in range(i):
        # 인접한 두 숫자의 위치를 바꿔보면서 더 큰 숫자로 만들 수 있는 순서로 정렬
        num1, num2 = numbers[j], numbers[j + 1]
        if int(num1 + num2) < int(num2 + num1):
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# 정렬된 숫자의 첫번째 값이 0일 경우에는 0을 출력
print("".join(numbers) if numbers[0] != "0" else 0)
