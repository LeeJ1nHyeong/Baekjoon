n, m = map(int, input().split())
ground = list(map(int, input().split()))

order = [0] * (n + 1)  # 조교의 지시에 따른 운동장 작업 위치 번호

# 조교의 지시에 따라 작업 위치의 처음 번호에는 작업량을 더해주고 끝 번호에 작업량 빼기
for _ in range(m):
    a, b, k = map(int, input().split())
    order[a - 1] += k
    order[b] -= k

change = 0  # 작업량

# 순서대로 운동장에 작업량 적옹
for i in range(n):
    change += order[i]
    ground[i] += change

# 작업 완료 후의 운동장 높이 출력
print(*ground)
