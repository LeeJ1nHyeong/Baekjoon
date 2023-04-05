X = int(input())

num = 1
a, b = 0, 0
n = 1
i = 0

while X >= num:
    i += 1

    if n%2 == 1:
        a = n - i + 1
        b = i

    else:
        a = i
        b = n - i + 1

    if n == i:
        n += 1
        i = 0
    num += 1

print(f'{a}/{b}')