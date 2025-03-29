n = int(input())
blossoms = list(map(int, input().split()))

max_p = 0

part1 = 1
for i in range(n - 3):
    part1 *= blossoms[i]

    part2 = 1
    for j in range(i + 1, n - 2):
        part2 *= blossoms[j]

        part3 = 1
        for k in range(j + 1, n - 1):
            part3 *= blossoms[k]

            part4 = 1
            for l in range(k + 1, n):
                part4 *= blossoms[l]

                p = part1 + part2 + part3 + part4
                max_p = max(max_p, p)

print(max_p)
