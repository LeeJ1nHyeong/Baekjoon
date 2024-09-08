n, m = map(int, input().split())
budget = []

for _ in range(n):
    budget.append(int(input()))

# 사용할 금액 중 최솟값을 시작점, 예산의 총 합을 끝점으로 시작
start, end = min(budget), sum(budget)

while start <= end:
    mid = (start + end) // 2

    # 중간값 금액 인출을 1회 진행한 상태로 시작
    cnt = 1
    charge = mid

    for i in range(n):
        # 잔액이 사용할 금액보다 낮다면 인출
        if budget[i] > charge:
            cnt += 1
            charge = mid

        # 금액 사용
        charge -= budget[i]

    # 인출 횟수가 m보다 크거나 중간값이 예산 최댓값보다 작다면 시작점 최신화
    if cnt > m or mid < max(budget):
        start = mid + 1

    # 인출 횟수가 m보다 작거나 같고 중간값이 예산 최댓값보다 크거나 같다면 ans를 중간값으로 저장 후 끝점 최신화
    else:
        ans = mid
        end = mid - 1

print(ans)
