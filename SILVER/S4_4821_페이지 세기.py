while True:
    n = int(input())
    if not n:
        break

    pages = list(input().split(","))
    visited = [0] * (n + 1)
    cnt = 0
    for page in pages:
        if "-" in page:
            start, end = page.split("-")
            if int(start) <= int(end):
                for i in range(int(start), int(end) + 1):
                    if i > n:
                        break

                    if not visited[i]:
                        visited[i] = 1
                        cnt += 1

        else:
            if int(page) > n:
                continue

            if not visited[int(page)]:
                visited[int(page)] = 1
                cnt += 1

    print(cnt)
