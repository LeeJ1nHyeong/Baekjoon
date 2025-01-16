r, c = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(r)]
t = int(input())

ans = 0
for i in range(r - 2):
    for j in range(c - 2):
        filter_image = []
        for a in range(3):
            for b in range(3):
                filter_image.append(image[i + a][j + b])

        filter_image.sort()
        if filter_image[4] >= t:
            ans += 1

print(ans)
