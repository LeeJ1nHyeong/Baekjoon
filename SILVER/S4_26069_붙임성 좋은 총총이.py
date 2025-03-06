n = int(input())
dance = set()

for _ in range(n):
    a, b = input().split()

    if a == "ChongChong" or b == "ChongChong":
        dance.add(a)
        dance.add(b)

    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))
