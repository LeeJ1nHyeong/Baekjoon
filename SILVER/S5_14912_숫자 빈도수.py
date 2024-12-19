n, d = map(int, input().split())
ans = 0

for i in range(1, n + 1):
    number = str(i)
    for j in number:
        if int(j) == d:
            ans += 1

print(ans)
