n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 두 배열 합치고 오름차순 정렬
ans = sorted(a + b)

print(*ans)
