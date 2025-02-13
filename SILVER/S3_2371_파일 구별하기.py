n = int(input())
files = []

for _ in range(n):
    file = list(map(int, input().split()))
    files.append(file[:len(file) - 1])

k = 1

while True:
    file_set = set()

    for file in files:
        if len(file) < k:
            file_set.add(tuple(file))
        else:
            file_set.add(tuple(file[:k]))

    if len(file_set) == n:
        break

    k += 1

print(k)
