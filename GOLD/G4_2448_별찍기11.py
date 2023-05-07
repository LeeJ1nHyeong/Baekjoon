import sys
input = sys.stdin.readline

def triangle(n, x, y):
    if n == 3:
        star[x][y] = '*'
        star[x + 1][y - 1] = star[x + 1][y + 1] = '*'
        for j in range(-2, 3):
            star[x + 2][y + j] = '*'

    else:
        triangle(n // 2, x, y)
        triangle(n // 2, x + n // 2, y - n // 2)
        triangle(n // 2, x + n // 2, y + n // 2)

N = int(input())
star = [[' ' for _ in range(2 * N)] for _ in range(N)]
triangle(N, 0, N - 1)
for s in star:
    print(''.join(s))