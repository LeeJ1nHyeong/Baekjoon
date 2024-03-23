n = int(input())
ropes = []

for _ in range(n):
    rope = int(input())
    ropes.append(rope)

ropes.sort()  # 로프 최대 중량 오름차순 정렬

ans = 0  # 로프를 활용하여 버틸 수 있는 최대 중량

for i in range(n):
    ans = max(ans, ropes[i] * (n - i))

print(ans)