n, m, q = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
row = [0] * n
column = [0] * m

for _ in range(q):
    num1, num2, num3 = map(int, input().split())

    if num1 == 1:
        r, v = num2, num3
        row[r - 1] += v

    else:
        c, v = num2, num3
        column[c - 1] += v
           
for i in range(n):
    for j in range(m):
        matrix[i][j] += row[i] + column[j]

for mat in matrix:
    print(*mat)
