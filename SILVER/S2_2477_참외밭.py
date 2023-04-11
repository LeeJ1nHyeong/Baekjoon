K = int(input())

row = []
column = []
total = []

for _ in range(6):
    d, length = map(int, input().split())
    if d == 1 or d == 2:
        row.append(length)
        total.append(length)
    elif d == 3 or d == 4:
        column.append(length)
        total.append(length)

max_field = max(row) * max(column)

sub_idx1, sub_idx2 = total.index(max(row)) + 3, total.index(max(column)) + 3

if sub_idx1 > 5:
    sub_idx1 -= 6
if sub_idx2 > 5:
    sub_idx2 -= 6

field = max_field - (total[sub_idx1] * total[sub_idx2])

print(field * K)