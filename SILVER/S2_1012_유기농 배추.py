import sys
sys.setrecursionlimit(10**6)

def backtrack(i, j, di, dj):
    global worm

    if 0 <= i + di < N and 0 <= j + dj < M:
        if field[i + di][j + dj] == 1:
            field[i + di][j + dj] = 0
            backtrack(i + di, j + dj, 0, 1)
            backtrack(i + di, j + dj, 1, 0)
            backtrack(i + di, j + dj, 0, -1)
            backtrack(i + di, j + dj, -1, 0)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    worm = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    visited = [[False] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                field[y][x] = 0
                backtrack(y, x, 0, 1)
                backtrack(y, x, 1, 0)
                backtrack(y, x, 0, -1)
                backtrack(y, x, -1, 0)
                worm += 1

    print(worm)