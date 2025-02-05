import sys

n = int(input())
numbers = sys.stdin.read()
range_total = sum(range(1, n))

total = 0
num = ""
for number in numbers:
    if number.isdigit():
        num += number
    else:
        total += int(num)
        num = ""

if num:
    total += int(num)

ans = total - range_total
print(ans)
