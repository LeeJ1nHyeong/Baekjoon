n, m = map(int, input().split())
packages = []
ones = []

for _ in range(m):
    package, one = map(int, input().split())
    packages.append(package)
    ones.append(one)

min_package = min(packages)
min_one = min(ones)

ans = 0

# 낱개 최솟값 6개가 패키지 최솟값보다 더 작다면 모든 기타줄을 낱개 최솟값으로 계산 
if min_package > min_one * 6:
    ans += min_one * n

else:
    ans += min_package * (n // 6) + min(min_package, min_one * (n % 6))

print(ans)
