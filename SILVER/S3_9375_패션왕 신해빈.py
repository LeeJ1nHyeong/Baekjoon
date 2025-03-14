t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}

    for _ in range(n):
        cloth, cloth_type = input().split()
        if cloth_type not in clothes:
            clothes[cloth_type] = [cloth]
        else:
            clothes[cloth_type].append(cloth)

    ans = 1
    for cloth_type in clothes:
        ans *= len(clothes[cloth_type]) + 1

    print(ans - 1)
