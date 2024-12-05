from collections import deque

tc = 0

while True:
    try:
        tc += 1

        n = int(input())
        carpet = [list(input()) for _ in range(n)]
        visited = [[0] * n for _ in range(n)]

        cnt = 0

        for i in range(n):
            for j in range(n):
                if carpet[i][j] == "0" or visited[i][j]:
                    continue

                queue = deque([(i, j)])
                visited[i][j] = 1

                while queue:
                    ci, cj = queue.popleft()

                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                        ni, nj = ci + di, cj + dj

                        if ni < 0 or ni == n or nj < 0 or nj == n:
                            continue

                        if carpet[ni][nj] == "0":
                            continue

                        if visited[ni][nj]:
                            continue

                        visited[ni][nj] = 1
                        queue.append((ni, nj))

                cnt += 1

        print(f"Case #{tc}: {cnt}")

    except:
        break
