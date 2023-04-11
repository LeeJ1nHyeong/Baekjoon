import sys

C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

seat = [[0] * R for _ in range(C)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

num = 0
k = 0
i, j = 0, 0

while True:
    num += 1
    if num == K:
        break
    seat[i][j] = num
    ni, nj = i + di[k], j + dj[k]
    if ni < 0 or ni == C or nj < 0 or nj == R or seat[ni][nj] != 0:
        k += 1
        if k > 3:
            k = 0
        ni, nj = i + di[k], j + dj[k]
    i, j = ni, nj

if C * R < K:
    print(0)

else:
    print(i + 1, j + 1)