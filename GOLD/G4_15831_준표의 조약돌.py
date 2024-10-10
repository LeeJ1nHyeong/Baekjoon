n, b, w = map(int, input().split())
stone = list(input())

left = 0  # 왼쪽 포인터
ans = 0  # 조건을 충족하는 범위 중 최대 길이

b_cnt, w_cnt = 0, 0  # 검은 조약돌, 흰 조약돌 개수

# 오른쪽 포인터 탐색
for right in range(n):
    # 오른쪽 포인터의 색깔에 따라 개수 증가
    if stone[right] == "W":
        w_cnt += 1
    else:
        b_cnt += 1

    # 검은 조약돌 개수가 b가 될 때까지 왼쪽 포인터 이동
    while b_cnt > b:
        if stone[left] == "W":
            w_cnt -= 1
        else:
            b_cnt -= 1

        left += 1

    # 흰 조약돌 개수가 w개 이상이라면 범위 최댓값 여부 확인
    if w_cnt >= w:
        ans = max(ans, right - left + 1)

print(ans)
