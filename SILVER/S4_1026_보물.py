n = int(input())
a = list(map(int, input().split()))
a.sort()  # 배열 a 오름차순 정렬
b = list(map(int, input().split()))
b.sort(reverse=True)  # 배열 b 내림차순 정렬

# a가 오름차순, b가 내림차순일 때 최솟값을 갖는다. 
ans = 0

for i in range(n):
    ans += a[i] * b[i]

print(ans)