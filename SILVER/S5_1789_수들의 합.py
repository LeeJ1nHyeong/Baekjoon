n = int(input())

cnt = 0
i = 0

while True:
    if n > i:
        i += 1
        n -= i
        cnt += 1

    else:
        print(cnt)
        break
