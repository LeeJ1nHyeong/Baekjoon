n = int(input())
ans = []

for i in range(1, n + 1):
    numbers = [n, i]

    while True:
        num = numbers[-2] - numbers[-1]

        if num < 0:
            break

        numbers.append(num)

    if len(numbers) > len(ans):
        ans = numbers

print(len(ans))
print(*ans)
