n = int(input())
board = [list(input()) for _ in range(n)]

max_i, max_j = n, n
ans = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == ".":
            total = 0

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                cnt = 0
                ni, nj = i, j
                while True:
                    ni += di
                    nj += dj

                    if ni < 0 or ni == n or nj < 0 or nj == n:
                        break

                    if board[ni][nj] == "W":
                        cnt += 1
                    elif board[ni][nj] == "B":
                        total += cnt
                        break
                    elif board[ni][nj] == ".":
                        break

            if total > ans:
                ans = total
                max_i, max_j = i, j

if not ans:
    print("PASS")
else:
    print(max_j, max_i)
    print(ans)
