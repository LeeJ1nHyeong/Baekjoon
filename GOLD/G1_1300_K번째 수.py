n = int(input())
k = int(input())

start, end = 1, n * n  # 배열에서 만들 수 있는 최솟값은 1, 최댓값은 n * n

while start <= end:
    mid = (start + end) // 2

    # mid 보다 작은 숫자가 몇 개인지 확인
    num = 0
    for i in range(1, n + 1):  # mid 값을 행 번호로 나눈 값과 행 개수 중 더 작은 값을 더함
        num += min(mid // i, n)

    if num >= k:  # k값보다 크거나 같으면 end를 1 줄임
        end = mid - 1
    else:  # k값보다 작으면 start를 1 증가
        start = mid + 1

print(start)