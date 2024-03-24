n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0  # 이동 최소 비용
min_price = price[0]  # 처음 가격을 기준으로 시작

# 현재 도시에서의 리터당 가격이 더 싸다면 그 가격을 최소 비용에 저장하고 다음 이동 거리를 곱하여 total에 더하기
for i in range(n - 1):
    if price[i] < min_price:
        min_price = price[i]

    total += min_price * distance[i]

print(total)  # 최소 비용 출력