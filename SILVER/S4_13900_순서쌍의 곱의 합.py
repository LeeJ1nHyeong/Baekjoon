n = int(input())
numbers = list(map(int, input().split()))

ans = (sum(numbers) ** 2 - sum(num * num for num in numbers)) // 2
print(ans)
