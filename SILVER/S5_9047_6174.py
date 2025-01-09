t = int(input())

for _ in range(t):
    number = int(input())
    ans = 0

    while number != 6174:
        ans += 1

        now = list(str(number))

        max_num = int("".join(sorted(now, reverse=True)))
        min_num = int("".join(sorted(now)))

        number = max_num - min_num

        if number < 1000:
            number *= 10 * (4 - len(str(number)))

    print(ans)
