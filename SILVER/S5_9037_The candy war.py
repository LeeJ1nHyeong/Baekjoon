def check(c):
    if len(set(candy)) == 1:
        return True

    return False


t = int(input())

for _ in range(t):
    n = int(input())
    candy = list(map(int, input().split()))

    cycle = 0
    while True:
        if check(candy):
            break

        next_candy = [0] * n

        for i in range(n):
            if candy[i] % 2:
                candy[i] += 1

        if check(candy):
            break

        for i in range(n):
            next_candy[(i + 1) % n] += candy[i] // 2
            next_candy[i] += candy[i] // 2

        candy = next_candy

        cycle += 1

    print(cycle)
