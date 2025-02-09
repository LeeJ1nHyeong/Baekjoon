n, k = map(int, input().split())
hamburger = list(input())

ans = 0

for i in range(n):
    if hamburger[i] == "P":
        for j in range(i - k, i + k + 1):
            if j < 0 or j >= n:
                continue

            if hamburger[j] == "H":
                ans += 1
                hamburger[j] = "."
                break

print(ans)
