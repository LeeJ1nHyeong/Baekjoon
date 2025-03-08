n = int(input())

ans = 0
while n > 0:
    # 남은 금액이 5의 배수가 될 때까지 2원으로 채운 뒤 5원으로 마무리
    if n % 5 == 0:
        ans += n // 5
        n -= 5 * (n // 5)
    else:
        ans += 1
        n -= 2

# 2원과 5원으로 거슬러줄 수 없으면 -1 출력
print(ans if n == 0 else -1)
