n = int(input())
numbers = list(map(int, input().split()))
ans = 0
pre_sum = 0

for i in range(n - 1):
    pre_sum += numbers[i]
    ans += pre_sum * numbers[i + 1]

print(ans)
