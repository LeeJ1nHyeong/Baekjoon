n = int(input())
budget = sorted(list(map(int, input().split())))  # 지방 예산들을 오름차순 정렬한 상태로 저장
m = int(input())  # 총 예산

ans = 0
start, end = 1, budget[-1]  # 시작점을 1, 끝점을 지방 예산 중 최댓값으로 시작

while start <= end:
    mid = (start + end) // 2

    # 지방 예산과 중간값 중 최솟값을 cnt에 추가
    cnt = 0
    for b in budget:
        cnt += min(mid, b)

    # 배정된 예산 총 합이 m보다 작거나 같다면 ans에 저장 후 시작점 최신화
    if cnt <= m:
        ans = mid
        start = mid + 1

    # m보다 크다면 끝점을 최신화
    else:
        end = mid - 1

# 배정된 예산 최댓값 출력
print(ans)
