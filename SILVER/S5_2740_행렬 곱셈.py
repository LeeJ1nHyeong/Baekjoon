n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

multiple = [[0] * k for _ in range(n)]

# 행렬 곱셈 진행
for x in range(n):
    for z in range(k):
        for y in range(m):
            multiple[x][z] += a[x][y] * b[y][z]

for mu in multiple:
    print(*mu)
