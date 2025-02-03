while True:
    try:
        n, m = map(int, input().split())
        cnt = 0
        for num in range(n, m + 1):
            num = str(num)
            num_set = set(num)

            if len(num) == len(num_set):
                cnt += 1

        print(cnt)

    except EOFError:
        break
