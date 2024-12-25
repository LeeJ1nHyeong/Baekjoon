t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    while True:
        is_change = False
        for i in range(n - 2):
            if s[i:i + 3] == "ABB":
                s = s[:i] + "BA" + s[i + 3:]
                is_change = True
                break

        if not is_change:
            break

    print(s)
