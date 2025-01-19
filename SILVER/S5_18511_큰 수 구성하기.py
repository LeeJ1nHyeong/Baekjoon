def recursion(num):
    if num > n:
        return

    if num > 0:
        new_numbers.append(num)

    for number in numbers:
        recursion(num * 10 + number)


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
new_numbers = []

recursion(0)

new_numbers.sort(reverse=True)
print(new_numbers[0])
