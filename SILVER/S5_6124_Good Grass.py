r, c = map(int, input().split())
grass = [list(map(int, input().split())) for _ in range(r)]

max_total = 0
si, sj = 0, 0
for i in range(r - 3):
    for j in range(c - 3):
        total = 0
        for a in range(3):
            for b in range(3):
                total += grass[i + a][j + b]

        if total > max_total:
            max_total = total
            si, sj = i, j
        elif total == max_total:
            if i > si:
                continue

            if i == si:
                if j > sj:
                    continue

            si, sj = i, j

print(max_total)
print(si + 1, sj + 1)
