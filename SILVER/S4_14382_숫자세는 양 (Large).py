t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    ans = "INSOMNIA"
    visited = set()

    for i in range(1, 101):
        target = str(n * i)

        for num in target:
            visited.add(num)

        if len(visited) == 10:
            ans = n * i
            break

    print(f"Case #{tc}: {ans}")
