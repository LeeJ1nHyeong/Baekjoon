n, m = map(int, input().split())
lesson = list(map(int, input().split()))

# 강의 길이의 최댓값과 강의 길이 전체 합을 양쪽 포인터로 시작
left, right = max(lesson), sum(lesson)
ans = 0  # m개의 블루레이를 만들 수 있는 길이의 최솟값

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    total = 0

    # 길이가 mid인 블루레이를 만들 수 있는 개수 탐색
    for i in range(n):
        if total + lesson[i] > mid:
            cnt += 1
            total = 0

        total += lesson[i]

    # m개 이하로 만들어 진다면 ans를 mid로 저장 후 오른쪽 포인터 최신화
    if cnt <= m:
        ans = mid
        right = mid - 1
    # 아니라면 왼쪽 포인터 최신화
    else:
        left = mid + 1

print(ans)
