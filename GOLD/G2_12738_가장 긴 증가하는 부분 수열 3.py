def binary_search(start, end, target):
    if start > end:
        return start

    while start <= end:
        mid = (start + end) // 2

        if partial[mid] == target:
            return mid

        elif partial[mid] > target:
            end = mid - 1
        elif partial[mid] < target:
            start = mid + 1

    return start


n = int(input())
numbers = list(map(int, input().split()))

partial = [numbers[0]]  # 최장 증가 부분 수열

for i in range(1, n):
    # 최장 증가 부분 수열의 최댓값보다 큰 값이면 그대로 추가
    if numbers[i] > partial[-1]:
        partial.append(numbers[i])

    # 그렇지 않다면 이분 탐색을 통해 해당 값의 크기 순서에 해당하는 인덱스를 구하여 최장 증가 부분 수열에 저장
    else:
        idx = binary_search(0, len(partial) - 1, numbers[i])
        partial[idx] = numbers[i]

print(len(partial))
