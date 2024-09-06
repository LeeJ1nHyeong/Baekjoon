def binary_search():
    ans = 0  # 랜선 길이 최댓값
    start, end = 1, line[-1]  # 1과 갖고 있는 랜선을 시작점, 끝점으로 설정

    # (시작점) > (끝점)이 될 때까지 이분 탐색(매개변수 탐색) 진행
    while start <= end:
        mid = (start + end) // 2

        # 각 랜선의 길이를 중간값으로 나눈 몫을 cnt에 추가
        cnt = 0
        for i in range(k):
            cnt += line[i] // mid

        # mid의 크기를 갖는 자른 랜선 개수가 n개 이상이라면 ans로 저장 후 시작점 최신화
        if cnt >= n:
            ans = mid
            start = mid + 1

        # n개 미만이라면 끝점 최신화
        else:
            end = mid - 1

    return ans  # 랜선 길이 최댓값 return


k, n = map(int, input().split())
line = []

for _ in range(k):
    line.append(int(input()))

# 랜선 오름차순 정렬 후 이분 탐색 진행
line.sort()
print(binary_search())
