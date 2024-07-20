n, m = map(int, input().split())
j = int(input())

ans = 0  # 바구니 최소 이동 횟수
now = 1  # 바구니의 가장 왼쪽 위치 번호
for _ in range(j):
    apple = int(input())
    # 사과가 바구니 위치에 떨어지면 이동 X
    if now <= apple <= now + m - 1:
        continue

    # 사과가 바구니 왼쪽에 떨어지면 왼쪽으로 이동
    if apple < now:
        ans += now - apple
        now = apple

    # 사과가 바구니 오른쪽으로 떨어지면 오른쪽으로 이동
    elif apple > now + m - 1:
        ans += apple - now - m + 1
        now = apple - m + 1

# 바구니 최소 이동 횟수 출력
print(ans)
