n = int(input())
numbers = list(map(int, input().split()))
sort_numbers = []

for number in numbers:
    if number not in sort_numbers:
        sort_numbers.append(number)

sort_numbers.sort()

print(*sort_numbers)
