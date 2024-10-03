n = int(input())

# 각 손님의 팁을 내림차순 정렬
tip = [int(input()) for _ in range(n)]
tip.sort(reverse=True)

ans = 0  # 최대로 받을 수 있는 팁

# 각 팁에 등수를 차감한 값 중 양수인 값을 ans에 추가
for i in range(n):
    t = tip[i] - i

    if t > 0:
        ans += t

print(ans)
