import sys
input = sys.stdin.readline

s, c = map(int, input().split())

# 파의 길이를 오름차순 정렬로 저장
green_onion = [int(input()) for _ in range(s)]
green_onion.sort()

cut = 0  # 파닭에 넣을 파 조각의 길이

# 시작점을 1, 끝점을 파 길이 중 최댓값으로 시작
start, end = 1, max(green_onion)

while start <= end:
    mid = (start + end) // 2

    cnt = 0  # 파닭에 넣은 파 조각 개수

    # 각 파의 길이를 중간값으로 나눈 몫을 cnt에 추가
    for i in range(s):
        cnt += green_onion[i] // mid

    # cnt가 c보다 크거나 같다면 cut을 mid로 저장 후 최댓값을 구하기 위해 시작점 최신화
    if cnt >= c:
        cut = mid
        start = mid + 1

    # cnt가 c보다 작다면 끝점 최신화
    else:
        end = mid - 1

# 파닭에 넣고 남은 파의 길이 합 출력
ans = sum(green_onion) - cut * c
print(ans)
