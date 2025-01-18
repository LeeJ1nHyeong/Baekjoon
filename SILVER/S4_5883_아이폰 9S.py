n = int(input())
b = [int(input()) for _ in range(n)]
set_b = set(b)

max_length = 1
for target in set_b:
    length = 0
    prev = 0

    for i in range(n):
        if b[i] == target:
            continue

        if b[i] == prev:
            length += 1
            max_length = max(length, max_length)
        else:
            length = 1
            prev = b[i]

print(max_length)
