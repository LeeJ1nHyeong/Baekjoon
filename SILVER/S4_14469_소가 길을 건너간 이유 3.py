n = int(input())
time = []

for _ in range(n):
    arrive, check = map(int, input().split())
    time.append((arrive, check))

# 도착 시간, 도착 시간이 같다면 검문 시간 오름차순으로 정렬
time.sort(key=lambda x: (x[0], x[1]))

ans = 0
for t in time:
    if ans <= t[0]:
        ans = t[0]
    ans += t[1]

print(ans)
