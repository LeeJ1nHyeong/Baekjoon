t = int(input())

for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    ans = 0  # 최대로 얻을 수 있는 수익
    max_price = 0  # 주식 가격 최댓값

    # 가격 목록을 역순으로 탐색
    for i in range(n - 1, -1, -1):
        # 가격이 최댓값이라면 최댓값 갱신
        if price[i] > max_price:
            max_price = price[i]
        # 최댓값이 아닐 경우 최댓값과 현재 가격의 차를 ans에 추가
        else:
            ans += max_price - price[i]

    # 최대로 얻을 수 있는 수익 출력
    print(ans)
