def binary_search():
    # 시작값을 1, 끝값을 최댓값으로 저장
    start, end = 1, height[-1]

    # 이진 탐색 진행
    while start <= end:
        # 두 값의 중간값
        mid = (start + end) // 2

        cut_height = 0  # 가져갈 나무의 합

        # 중간값보다 크거나 같은 값에 대해 가져갈 나무의 합을 구하기
        for h in height:
            if h >= mid:
                cut_height += h - mid

        # 가져갈 나무의 합이 목표값보다 크거나 같다면 start를 mid + 1로 저장
        if cut_height >= m:
            start = mid + 1
        # 가져갈 나무의 합이 목표값보다 작다면 end를 mid - 1로 저장
        elif cut_height < m:
            end = mid - 1

    return end  # while문 종료 후 end를 return


n, m = map(int, input().split())
height = list(map(int, input().split()))
height.sort()  # 오름차순으로 정렬

print(binary_search())  # 이진 탐색 진행
